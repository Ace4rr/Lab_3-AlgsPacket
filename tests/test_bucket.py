import pytest
from sorts.bucket import bucket_sort

def test_bucket_simple():
    arr=[0.4, 0.1, 0.3, 0.2]
    assert bucket_sort(arr)==sorted(arr)

def test_bucket_integers():
    arr=[7, 3, 1, 9, 4]
    assert bucket_sort(arr)==[1, 3, 4, 7, 9]

def test_bucket_duplicates():
    arr=[5, 1, 5, 3, 1]
    assert bucket_sort(arr)==[1, 1, 3, 5, 5]

def test_bucket_reverse():
    arr=[9, 8, 7, 6, 5]
    assert bucket_sort(arr)==[5, 6, 7, 8, 9]

def test_bucket_single():
    arr=[42]
    assert bucket_sort(arr)==[42]

def test_bucket_empty():
    arr=[]
    assert bucket_sort(arr)==[]