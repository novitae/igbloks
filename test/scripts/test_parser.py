import pytest

from igbloks.scripts.parser import parse

def test_parse():
    with pytest.raises(IndexError):
        parse(' (funcanme, 6, (funcsub, 8)')
    with pytest.raises(AssertionError):
        parse(' funcanme, 6, (funcsub, 8))')
    with pytest.raises(AssertionError):
        parse('(funcanme, 678')
    assert parse('(funcanme, true, (subfunc, false, (subsub, 89272, "hello")), null)') == {'funcanme': [True, {'subfunc': [False, {'subsub': [89272, 'hello']}]}, None]}
