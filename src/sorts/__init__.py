from .bubble import bubble_sort
from .quick import quick_sort
from .counting import counting_sort
from .radix import radix_sort
from .bucket import bucket_sort
from .heap import heap_sort

def run_sort(algo, nums):
    if algo=="bubble":
        return bubble_sort(nums)
    if algo=="quick":
        return quick_sort(nums)
    if algo=="count":
        return counting_sort(nums)
    if algo=="radix":
        return radix_sort(nums)
    if algo=="bucket":
        return bucket_sort(nums)
    if algo=="heap":
        return heap_sort(nums)
    raise ValueError(f"Unknown sort algorithm: {algo}")