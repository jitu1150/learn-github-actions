import pytest
import OM

from calculator import add, divide

print("Running  test_calculator.py - github-jitu\\learn-github-actions")
def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
