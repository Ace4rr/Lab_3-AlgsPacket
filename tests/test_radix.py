import pytest
from sorts.radix import radix_sort

def test_radix_simple():
    arr=[3, 1, 2]
    assert radix_sort(arr)==[1, 2, 3]

def test_radix_sorted():
    arr=[1, 2, 3, 4]
    assert radix_sort(arr)==[1, 2, 3, 4]

def test_radix_reverse():
    arr=[9, 7, 5, 3, 1]
    assert radix_sort(arr)==[1, 3, 5, 7, 9]

def test_radix_duplicates():
    arr=[4, 2, 4, 1, 2]
    assert radix_sort(arr)==[1, 2, 2, 4, 4]

def test_radix_large_numbers():
    arr=[329, 457, 657, 839, 436, 720, 355]
    assert radix_sort(arr)==sorted(arr)

def test_radix_single():
    arr=[100]
    assert radix_sort(arr)==[100]

def test_radix_empty():
    arr=[]
    assert radix_sort(arr)==[]