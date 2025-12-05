import pytest
from algos.fibonacci import fibo, fibo_recursive

def test_fibo_basic():
    assert fibo(0)==0
    assert fibo(1)==1
    assert fibo(5)==5
    assert fibo(10)==55

def test_fibo_recursive_basic():
    assert fibo_recursive(0)==0
    assert fibo_recursive(1)==1
    assert fibo_recursive(6)==8
    assert fibo_recursive(7)==13

def test_fibo_matches_recursive():
    for n in range(10):
        assert fibo(n)==fibo_recursive(n)

def test_fibo_negative():
    with pytest.raises(ValueError):
        fibo(-1)

def test_fibo_recursive_negative():
    with pytest.raises(ValueError):
        fibo_recursive(-5)