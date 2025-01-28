from typing import Any, Callable, Dict, List

functions_map: Dict[str, Callable[[Any], Any]] = {}

def blok_function(name: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    A decorator that registers a function in a global dictionary `d` under the specified name.

    Args:
        name (str): The key under which the function will be registered in the dictionary `d`.

    Returns:
        Callable: The decorated function.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        functions_map[name] = func
        return func
    return decorator

def run(d: Dict[str, Any]):
    assert len(d) == 1
    for key, value in d.items():
        if key in functions_map:
            return functions_map[key](*value)
        else:
            raise NotImplementedError(f'The function `"{key}"` is not yet implemented !')

def run_raw(o: Any):
    if isinstance(o, dict):
        return run(o)
    else:
        return o
    
def run_raw_many(l: List[Any]):
    return [run_raw(o=o) for o in l]
