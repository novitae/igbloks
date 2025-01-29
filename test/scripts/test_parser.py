import pytest

from igbloks.scripts.parser import parse_script

def test_parse():
    with pytest.raises(IndexError):
        parse_script(' (funcanme, 6, (funcsub, 8)')
    with pytest.raises(AssertionError):
        parse_script(' funcanme, 6, (funcsub, 8))')
    with pytest.raises(AssertionError):
        parse_script('(funcanme, 678')
    assert parse_script('(funcanme, true, (subfunc, false, (subsub, 89272, "hello")), null)') == {'funcanme': [True, {'subfunc': [False, {'subsub': [89272, 'hello']}]}, None]}
