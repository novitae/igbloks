from typing import Callable, Any
import ujson
from pydantic import BaseModel

from .parser import deserialize

class Cache(BaseModel):
    device_id: str = None
    waterfall_id: str = None
    is_dark_mode_enabled: bool = False

operands: dict[str, Callable] = {}

def execute(
    parsed_script: list[str, Any],
    cache: Cache = None,
    data: dict = None,
) -> Any:
    """Execute a script.

    Args:
        parsed_script (list[str, Any]): The script to execute.
        cache (Cache, optional): The cache, being a Cache object, used to fill values \
            such as the deviceid. Defaults to None.
        data (dict, optional): The full bloks response at ["layout"]["bloks_payload"]. \
            Defaults to None.

    Raises:
        NotImplementedError: The instruction is not supported yet.

    Returns:
        Any: The result of the execution.
    """
    cache = Cache() if cache is None else cache

    instruction, arguments = parsed_script[0], parsed_script[1:]
    new_arguments = [(execute(argument, cache) if isinstance(argument, list) and len(arguments) else argument) for argument in arguments]
    if instruction in operands:
        return operands[instruction]( *new_arguments,
                                      cache=cache,
                                      data=data,
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
    
@operand('bk.action.bloks.GetScript')
def bloksgetscript(*args, data: dict, **kwargs):
    assert data is not None, 'data must be specified to execute "bk.action.bloks.GetScript" command'
    return execute(deserialize(data["ft"][args[0]]), data=data, **kwargs)

@operand('bk.action.bloks.GetVariable2')
def bloksgetvariable(*args, data: dict, **kwargs):
    assert data is not None, 'data must be specified to execute "bk.action.bloks.GetVariable2" command'
    var_id = args[0]
    for item in data["data"]:
        if item["id"] == var_id:
            # key, type, ..., must be investigate further
            return item["initial"]
    else:
        raise KeyError(f'value of id "{var_id}" not found')
    
@operand('ig.action.IsDarkModeEnabled')
def actionisdarkmodeenable(*args, cache: Cache, **kwargs):
    return cache.is_dark_mode_enabled

@operand('bk.action.mins.CallRuntime')
def minscallruntime(*args, **kwargs):
    runtime, args = int(args[0]), args[1:]
    if runtime == 6:
        if args:
            return {args[0]: args[1]}
        else:
            return {}
    else:
        raise ValueError(f'unknown runtime "{runtime}"')
    
# @operand("bk.action.core.If")
# def coreif(*args, )

# @operand('bk.action.i32.Eq')
# def i32eq(*args, **kwargs):
#     return 