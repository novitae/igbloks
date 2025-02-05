import re

__all__ = ("is_custom_function_name", )

_re_custom_function_name = re.compile(r"^[\w\-]{22}:[a-z\d]{10}$")
def is_custom_function_name(s: str):
    """Tells if the given custom function name `s` is matching the criterias.

    Args:
        s (str): The custom function name.

    Returns:
        bool: Is it matching criterias ?
    """
    return bool(_re_custom_function_name.match(s))