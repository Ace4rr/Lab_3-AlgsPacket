import pytest
from sorts.counting import counting_sort

def test_counting_simple():
    arr=[3, 1, 2]
    assert counting_sort(arr)==[1, 2, 3]

def test_counting_with_duplicates():
    arr=[4, 2, 4, 1, 2]
    assert counting_sort(arr)==[1, 2, 2, 4, 4]

def test_counting_negative():
    arr=[0, -2, -1, -2, 3]
    assert counting_sort(arr)==[-2, -2, -1, 0, 3]

def test_counting_sorted():
    arr=[1, 2, 3, 4]
    assert counting_sort(arr)==[1, 2, 3, 4]

def test_counting_reverse():
    arr=[5, 4, 3, 2, 1]
    assert counting_sort(arr)==[1, 2, 3, 4, 5]

def test_counting_single():
    arr=[99]
    assert counting_sort(arr)==[99]

def test_counting_empty():
    arr=[]
    assert counting_sort(arr)==[]