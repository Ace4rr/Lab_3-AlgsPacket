from logger import logger

def quick_sort(arr):
    """
        Быстрая сортировка

        Args:
            arr

        Returns:
            arr
        """
    logger.debug(f"quick_sort input: {arr}")
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr) // 2]
    left=[x for x in arr if x < pivot]
    middle=[x for x in arr if x == pivot]
    right=[x for x in arr if x > pivot]
    sorted_arr=quick_sort(left) + middle + quick_sort(right)
    logger.debug(f"quick_sort output: {sorted_arr}")
    return sorted_arr
