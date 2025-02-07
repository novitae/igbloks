from typing import Any

from .runner import blok_function, run_raw_many, run_raw, BloksScriptRunner

@blok_function("bk.action.array.Concat")
def array_concat(*args, bsr):
    return sum(run_raw_many(*args, bsr=bsr), start=[])

@blok_function('bk.action.array.Make')
def array_make(*args, bsr):
    return list(run_raw_many(*args, bsr=bsr))

@blok_function("bk.action.array.Length")
def array_length(*args, bsr):
    assert len(args) == 1, f"There should be only one argument being the list to get the length from, {args=}"
    return len(run_raw(args[0], bsr=bsr))


@blok_function("bk.action.core.GetArg")
def core_getarg(*args, bsr: BloksScriptRunner):
    assert len(args) == 1
    return bsr.call_stack[-1].args[args[0]]

@blok_function("bk.action.core.SetArg")
def core_getarg(*args, bsr: BloksScriptRunner):
    assert len(args) == 2
    bsr.call_stack[-1].args[args[0]] = args[1]
    return


@blok_function("bk.action.map.Make")
def make_map(*args, bsr):
    return dict(zip(*run_raw_many(*args, bsr=bsr)))
