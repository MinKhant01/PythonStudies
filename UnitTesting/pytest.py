import pytest

def add(a, b):
    return a + b
"""
def test_add():
    assert add(1,3) == 4
"""
@pytest.mark.parameterize("a, b, expected", [1,2,3], [5,5,10], [0,0,0])
def test_add(a, b, expected):
    assert add(a, b) == expected


