from igbloks.scripts.executor import run_script

def test_array_make():
    assert run_script({"bk.action.array.Make": []}) == []
    assert run_script({"bk.action.array.Make": ["hello", "world"]}) == ["hello", "world"]
    assert run_script({"bk.action.array.Make": ["hello", {"ret": ["world"]}]}) == ["hello", "world"]

def test_array_length():
    assert run_script({"bk.action.array.Length": [{"bk.action.array.Make": []}]}) == 0
    assert run_script({"bk.action.array.Length": [{"bk.action.array.Make": ["hello", "hi"]}]}) == 2

def test_array_concat():
    assert run_script({"bk.action.array.Concat": [{"bk.action.array.Make": ["hello", "hi"]}, {"bk.action.array.Make": ["world"]}]}) == ["hello", "hi", "world"]
    assert run_script({"bk.action.array.Concat": []}) == []

def test_map_make():
    assert run_script({"bk.action.map.Make": [["hello"], ["world"]]}) == {"hello": "world"}
