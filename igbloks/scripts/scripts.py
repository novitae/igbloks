from typing import Callable, Any

import ujson

operands: dict[str, Callable] = {}

def execute(parsed_script: list[str, Any]):
    instruction, arguments = parsed_script[0], parsed_script[1:]
    new_arguments = [(execute(argument) if isinstance(argument, list) and len(arguments) else argument) for argument in arguments]
    if instruction in operands:
        return operands[instruction](*new_arguments)
    else:
        raise NotImplementedError(f'the method "{instruction}" is not implemented')

def operand(*operand_names: str):
    def decorator(f: Callable[..., Any]):
        for operand_name in operand_names:
            operands[operand_name] = f
        return f
    return decorator

@operand('bk.action.array.Make')
def arraymake(*args):
    return list(args)

@operand('bk.action.bool.Const')
def boolconst(*args):
    return bool(args[0])

@operand('bk.action.i32.Const')
def i32const(*args):
    return int(args[0])

@operand('bk.action.map.Make')
def mapmake(*args):
    assert len(args) == 2
    return dict(zip(*args))

@operand('bk.action.string.JsonEncode')
def stringjsonencode(*args):
    return ujson.dumps(args[0])
