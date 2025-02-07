from typing import Any, Callable, Dict, TYPE_CHECKING, Optional, NamedTuple
from collections import deque

if TYPE_CHECKING:
    from ...core import BloksPayload
else:
    class BloksPayload: pass

from ..parser import PARSED_FUNCTION, PARSED_FUNCARGS

functions_map: Dict[str, Callable[[Any], Any]] = {}

class CallFrame(NamedTuple):
    func: str
    args: PARSED_FUNCARGS

class BloksScriptRunner:
    __slots__ = ("bp", "call_stack")

    def __init__(
        self,
        bp: Optional[BloksPayload] = None,
    ):
        self.bp = bp
        self.call_stack: deque[CallFrame] = deque([])

    def __repr__(self):
        return "BloksScriptRunner({})".format(", ".join([
            "bp=" + str(None if self.bp is None else id(self.bp)),
        ]))

def blok_function(*names: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    A decorator that registers a function in a global dictionary `d` under the specified name.

    Args:
        name (str): The key under which the function will be registered in the dictionary `d`.

    Returns:
        Callable: The decorated function.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        for name in names:
            functions_map[name] = func
        return func
    return decorator

def run_script(d: PARSED_FUNCTION, bsr: Optional[BloksScriptRunner] = None):
    """Runs a blok script that was parsed using `igbloks.scripts.parse_script`.

    Args:
        d (PARSED_FUNCTION): The parsed script.
        bsr (BloksScriptRunner, optional): The `BloksScriptRunner` to track execution.
            Default to None.

    Raises:
        NotImplementedError: One of the methods encountered is not currently
            supported by the runner.

    Returns:
        Any: The results can be very different.
    """
    assert len(d) == 1
    for key, value in d.items():
        break
    if bsr is None:
        bsr = BloksScriptRunner()
    try:
        bsr.call_stack.append(CallFrame(func=key, args=value))
        if key.startswith("#"):
            # Something like `"#ScIZ5H-rY3SSDtflJUepGg:1hf0qfbdp4"` or `#1zcqnewoit`.
            if bsr.bp is None:
                raise ValueError( f"Custom function detected (`'{key}'`). "
                                    "It requires a `bp` to be set." )
            elif key not in bsr.bp.functions:
                raise NotImplementedError( f'The function `"{key}"` is not present in '
                                            'the custom functions map (`.ft`).' )
            else:
                raise NotImplementedError('Custom functions not yet possible to run.')
        elif key in functions_map:
            return functions_map[key](*value, bsr=bsr)
        else:
            raise NotImplementedError(f'The function `"{key}"` is not yet implemented !')
    finally:
        bsr.call_stack.pop()

def run_raw(o: Any, bsr: BloksScriptRunner):
    if isinstance(o, dict):
        return run_script(d=o, bsr=bsr)
    else:
        return o
    
def run_raw_many(*l: PARSED_FUNCTION, bsr: BloksScriptRunner):
    return [run_raw(o=o, bsr=bsr) for o in l]
