import pytest
from sorts.quick import quick_sort

def test_quick_simple():
    arr=[3, 1, 2]
    assert quick_sort(arr)==[1, 2, 3]

def test_quick_sorted():
    arr=[1, 2, 3, 4]
    assert quick_sort(arr)==[1, 2, 3, 4]

def test_quick_reverse():
    arr=[5, 4, 3, 2, 1]
    assert quick_sort(arr)==[1, 2, 3, 4, 5]

def test_quick_duplicates():
    arr=[4, 2, 4, 1, 2]
    assert quick_sort(arr)==[1, 2, 2, 4, 4]

def test_quick_single():
    arr=[42]
    assert quick_sort(arr)==[42]

def test_quick_empty():
    arr=[]
    assert quick_sort(arr)==[]