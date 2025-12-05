import pytest
from sorts.bubble import bubble_sort

def test_bubble_simple():
    arr=[3, 1, 2]
    assert bubble_sort(arr)==[1, 2, 3]

def test_bubble_sorted():
    arr=[1, 2, 3, 4]
    assert bubble_sort(arr)==[1, 2, 3, 4]

def test_bubble_reverse():
    arr=[5, 4, 3, 2, 1]
    assert bubble_sort(arr)==[1, 2, 3, 4, 5]

def test_bubble_duplicates():
    arr=[4, 2, 4, 1, 2]
    assert bubble_sort(arr)==[1, 2, 2, 4, 4]

def test_bubble_single():
    arr=[10]
    assert bubble_sort(arr)==[10]

def test_bubble_empty():
    arr=[]
    assert bubble_sort(arr)==[]