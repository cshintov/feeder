""" Tests for utilities """
from ..utils import *

def test_shape():
    assert shape({}) == {}
    assert shape({'a': {}}) == {'a': {}}
    assert shape({'a': 1}) == {'a': int}
    assert shape({'a': 'a'}) == {'a': str}
    assert shape({'a': {'b': 1}}) == {'a': {'b': int}}
    assert shape({'a': {'b': 1}, 'c': [2]}) == {'a': {'b': int}, 'c': [int]}
