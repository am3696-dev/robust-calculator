import pytest
from calculator.app import add, subtract, multiply, divide

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add_param(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (5, 2, 3),
    (2, 5, -3),
    (0, 0, 0)
])
def test_subtract_param(a, b, expected):
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (3, 4, 12),
    (-2, 3, -6),
    (0, 10, 0)
])
def test_multiply_param(a, b, expected):
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5),
    (5, 2, 2.5)
])
def test_divide_param(a, b, expected):
    assert divide(a, b) == expected

@pytest.mark.parametrize("a,b", [
    (5, 0),
    (10, 0)
])
def test_divide_zero(a, b):
    with pytest.raises(ValueError):
        divide(a, b)

