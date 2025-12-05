import pytest
from algos.factorial import factorial, factorial_recursive

def test_factorial_basic():
    assert factorial(0)==1
    assert factorial(1)==1
    assert factorial(5)==120
    assert factorial(7)==5040

def test_factorial_recursive_basic():
    assert factorial_recursive(0)==1
    assert factorial_recursive(1)==1
    assert factorial_recursive(6)==720
    assert factorial_recursive(8)==40320

def test_factorial_matches_recursive():
    for n in range(10):
        assert factorial(n)==factorial_recursive(n)

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-3)

def test_factorial_recursive_negative():
    with pytest.raises(ValueError):
        factorial_recursive(-9)