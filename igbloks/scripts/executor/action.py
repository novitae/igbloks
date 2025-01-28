from typing import Any

from .runner import blok_function, run_raw_many, run_raw

# array

@blok_function('bk.action.array.Make')
def array_make(*args: Any):
    return list(run_raw_many(args))

# map

@blok_function("bk.action.map.Make")
def make_map(*args: Any):
    return dict(zip(*run_raw_many(args)))
