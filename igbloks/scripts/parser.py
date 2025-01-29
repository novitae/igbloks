import orjson
from typing import Callable, Dict, Any

def is_script(s: str):
    return s.startswith(" (") and s.endswith(")")

def consume_callback(s: str, x: int, callback: Callable[[str], bool]):
    ls = len(s) - 1
    while x < ls and callback(s[x]):
        x += 1
    return x

def skip_spaces(s: str, x: int):
    return consume_callback(s=s, x=x, callback=str.isspace)

def try_consume_value(s: str, x: str, v: str, callback: Callable[[str], bool]):
    lv = len(v)
    if s.startswith(v, x) and callback(s[x + lv]) is False:
        return x + lv
    
def parse_string(s: str, x: str):
    consecutive_backlash = 0
    y = x+1
    while True:
        c = s[y]
        if c == '"' and consecutive_backlash % 2 == 0:
            break
        elif c == "\\":
            consecutive_backlash += 1
        else:
            consecutive_backlash = 0
        y += 1
    y += 1
    assert (c := s[y+1]) in ")," or c.isspace(), f"Found an invalidly terminated string at pos {y} with char {s[y]} (in '`{s[y-5:y+5]}`')"
    return y, orjson.loads(s[x:y])

def internal_parse(s: str, x: int):
    result = []
    x = skip_spaces(s, x)
    assert s[x] == "("
    x += 1
    while True:
        z = x
        x = skip_spaces(s, x)
        c = s[x]
        if c == ",":
            x += 1
            continue
        elif c == ")":
            break
        elif c == "(":
            x, value = internal_parse(s=s, x=x)
        elif c == '"':
            x, value = parse_string(s=s, x=x)
        elif c.isalnum():
            y = consume_callback(s=s, x=x, callback=lambda v: v.isalnum() or v == ".")
            value = s[x:y]
            if value.isdigit():
                value = int(value)
            elif value == "true":
                value = True
            elif value == "false":
                value = False
            elif value == "null":
                value = None
            x = y
        else:
            raise ValueError(s[x:])
        assert z != x, "Position didn't move, prevented an infinite loop"
        result.append(value)
    assert c == ")"
    return x+1, {result.pop(0): result}

def parse_script(s: str) -> Dict[str, list[Any]]:
    x, result = internal_parse(s=s, x=0)
    assert x == len(s), "The parsing wasn't fully completed"
    return result