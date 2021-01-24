""" Tests for content module """
import pytest
from ..content import *

@pytest.fixture
def html():
    url = 'http://www.paulgraham.com/earnest.html'
    return get_content(url)

def test_get_content(html):
    assert type(html) == str
    assert 'December 2020' in html
