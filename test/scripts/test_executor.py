from igbloks.scripts.executor import run_script, functions_map

# Test func
def _ret(*args):
    return args[0]
functions_map["ret"] = _ret

def test_map_make():
    assert run_script({"bk.action.map.Make": [["hello"], ["world"]]}) == {"hello": "world"}

def test_array_make():
    assert run_script({"bk.action.array.Make": []}) == []
    assert run_script({"bk.action.array.Make": ["hello", "world"]}) == ["hello", "world"]
    assert run_script({"bk.action.array.Make": ["hello", {"ret": ["world"]}]}) == ["hello", "world"]

def test_large():
    assert run_script({'bk.action.map.Make': [{'bk.action.array.Make': ['target_ig_user_id',
        'event_name',
        'referer_type',
        'surface',
        'bloks_app_id']},
      {'bk.action.array.Make': [0,
        'ata_help_center_click',
        'ProfileUsername',
        'Landing',
        'com.bloks.www.ig.about_this_account']}]}) == {'target_ig_user_id': 0,
        'event_name': 'ata_help_center_click',
        'referer_type': 'ProfileUsername',
        'surface': 'Landing',
        'bloks_app_id': 'com.bloks.www.ig.about_this_account'}