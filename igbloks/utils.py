from types import UnionType
from typing import Callable, Any

__all__ = ( "is_bkid", "branch_name", "is_branch", "annotation_types",
            "Undefined", "check_return_type", )

def is_bkid(__s: str, /) -> bool:
    return True
    try:
        return len(bytes.fromhex(s)) == 32
    except:
        return False
    
def branch_name(__d: dict, /) -> str | None:
    if isinstance(__d, dict):
        for key, value in __d.items():
            if isinstance(key, str) and isinstance(value, dict):
                break
        else:
            return
        return key   
    
def is_branch(__d: dict, /) -> bool:
    return bool(branch_name(__d))

def is_branch_list(__l: list, /) -> bool:
    if isinstance(__l, list):
        return all([is_branch(item) for item in __l])
    else:
        return False
    
def annotation_types(a) -> tuple[type]:
    if isinstance(a, type):
        return (a, )
    elif isinstance(a, UnionType):
        return a.__args__
    else:
        return ()

class _Undefined:
    def __repr__(self) -> str:
        return "Undefined()"
    
    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)
    
    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, self.__class__)
    
Undefined = _Undefined()


def check_return_type(func: Callable) -> Callable:
    def wrapper(self: object, *args: Any, **kwargs: Any):
        result = func(self, *args, **kwargs)
        if hasattr(self, 'skip_type_verif') and hasattr(self, 'accepted_types'):
            if self.skip_type_verif is False:
                if not isinstance(result, self.accepted_types):
                    raise TypeError( f'the result of "{func.__name__}" is of type '
                                     f'"{type(result)}", but should instance of '
                                     f'"{self.accepted_types}"' )
        return result
    return wrapper
