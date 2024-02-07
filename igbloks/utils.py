from types import UnionType
from typing import Callable, Any, TYPE_CHECKING
from enum import Enum

if TYPE_CHECKING:
    from .bloks._branches import BlokField
else:
    class BlokField: pass

__all__ = ( "is_bkid", "get_branch_name", "is_branch", "annotation_types",
            "Undefined", "check_return_type", "is_branch_list", "rgb_to_hex",
            "hex_to_rgb", "enum_list", )

def is_bkid(__s: str, /) -> bool:
    return True
    try:
        return len(bytes.fromhex(s)) == 32
    except:
        return False
    
def is_branch(__d: dict, /) -> bool:
    """Tells if a dict is a raw branch.

    Args:
        __d (dict): The dictionnary to check.

    Returns:
        bool: True if is a branch, else False.
    """
    return (isinstance(__d, dict) and len(__d) == 1) or (isinstance(__d, tuple) and len(__d) == 2 and isinstance(__d[1], dict))
    
def get_branch_name(__d: dict, /, *, verified_branch: bool = False) -> str | None:
    """Returns the branch name of the given raw branch dict.

    Args:
        __d (dict): The raw branch dict to return the name from.
        verified_branch (bool, optional): True if the branch was \
            verified, will avoid checking again. Defaults to False.

    Returns:
        str | None: The branch name, or None if it is not a branch.
    """
    if verified_branch is False and is_branch(__d) is False:
        return
    else:
        return next(iter(__d.keys()))
    
def is_branch_list(__l: list | tuple | set, /) -> bool:
    """Tells if a list is containing only raw branches.

    Args:
        __l (list | tuple | set): The list to check.

    Returns:
        bool: True if the list is full or raw branches, else False.
    """
    if isinstance(__l, (list, tuple, set)):
        return all(is_branch(item) for item in __l)
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


def check_return_type(func) -> Callable:
    def wrapper(self: BlokField, *args: Any, **kwargs: Any):
        result = func(self, *args, **kwargs)
        if hasattr(self, 'skip_type_verif') and hasattr(self, 'accepted_types'):
            if self.skip_type_verif is False:
                check_type = lambda item: isinstance(item, self.accepted_types) or item is Undefined
                if isinstance(result, list) and self.is_list:
                    if not all([check_type(item) for item in result]):
                        raise TypeError( '' )
                elif not check_type(result):
                    raise TypeError( f'the result of "{func.__name__}" is of type '
                                    f'"{type(result)}", but should instance of '
                                    f'"{self.accepted_types}"' )
        return result
    return wrapper

def rgb_to_hex(color: list[int]) -> str:
    return ("#" + "{:02x}" * len(color)).format(*color)

def hex_to_rgb(hex_color: str) -> tuple[int]:
    hex_color = hex_color.lstrip('#')
    length = len(hex_color)
    return tuple(int(hex_color[i:i+length//3], 16) for i in range(0, length, length//3))

def enum_list(e: Enum) -> list[Any]:
    return [item.value for item in e]