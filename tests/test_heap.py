import pytest
from sorts.heap import heap_sort

def test_heap_simple():
    arr=[3, 1, 2]
    assert heap_sort(arr)==[1, 2, 3]

def test_heap_sorted():
    arr=[1, 2, 3, 4]
    assert heap_sort(arr)==[1, 2, 3, 4]

def test_heap_reverse():
    arr=[5, 4, 3, 2, 1]
    assert heap_sort(arr)==[1, 2, 3, 4, 5]

def test_heap_duplicates():
    arr=[4, 2, 4, 1, 2]
    assert heap_sort(arr)==[1, 2, 2, 4, 4]

def test_heap_single():
    arr=[99]
    assert heap_sort(arr)==[99]

def test_heap_empty():
    arr=[]
    assert heap_sort(arr)==[]