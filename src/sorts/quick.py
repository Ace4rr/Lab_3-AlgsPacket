from logger import logger
import random 
import sys
sys.setrecursionlimit(1000**3)

def quick_sort(arr):
    """
        Быстрая сортировка

        Args:
            arr

        Returns:
            arr
        """
    if len(arr)<=1:
        return arr
    logger.debug(f"quick_sort input: {arr}")
    piv=random.randint(1,len(arr)-2)
    pivot=arr[piv]
    left=[x for x in arr if x < pivot]
    middle=[x for x in arr if x == pivot]
    right=[x for x in arr if x > pivot]
    sorted_arr=quick_sort(left) + middle + quick_sort(right)
    logger.debug(f"quick_sort output: {sorted_arr}")
    return sorted_arr

#реализован случайный выбор pivot'а