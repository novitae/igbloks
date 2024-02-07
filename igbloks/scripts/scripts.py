from typing import Callable, Any
import ujson
from pydantic import BaseModel

class Cache(BaseModel):
    device_id: str = None
    waterfall_id: str = None

operands: dict[str, Callable] = {}

def execute(parsed_script: list[str, Any], cache: Cache = None):
    cache = Cache() if cache is None else cache

    instruction, arguments = parsed_script[0], parsed_script[1:]
    new_arguments = [(execute(argument, cache) if isinstance(argument, list) and len(arguments) else argument) for argument in arguments]
    if instruction in operands:
        return operands[instruction]( *new_arguments,
                                      cache=cache,
                                      operand=instruction, )
    else:
        raise NotImplementedError(f'the method "{instruction}" is not implemented')

def operand(*operand_names: str):
    def decorator(f: Callable[..., Any]):
        for operand_name in operand_names:
            operands[operand_name] = f
        return f
    return decorator

@operand('bk.action.array.Make')
def arraymake(*args, **kwargs):
    return list(args)

@operand('bk.action.bool.Const')
def boolconst(*args, **kwargs):
    return bool(args[0])

@operand( 'bk.action.i32.Const',
          'bk.action.i64.Const', )
def i32const(*args, **kwargs):
    return int(args[0])

@operand('bk.action.map.Make')
def mapmake(*args, **kwargs):
    assert len(args) == 2
    return dict(zip(*args))

@operand('bk.action.string.JsonEncode')
def stringjsonencode(*args, **kwargs):
    return ujson.dumps(args[0])

@operand( 'bk.action.caa.login.GetUniqueDeviceId',
          'bk.fx.action.GetFamilyDeviceId',
          'bk.action.caa.GetWaterfallId', )
def fromcache(*args, cache: Cache, operand: str, **kwargs):
    if operand in ('bk.action.caa.login.GetUniqueDeviceId', 'bk.fx.action.GetFamilyDeviceId'):
        return cache.device_id
    elif operand == 'bk.action.caa.GetWaterfallId':
        return cache.waterfall_id