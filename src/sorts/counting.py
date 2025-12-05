from logger import logger

def counting_sort(arr):
    """
        Сортировка подсчетом

        Args:
            arr

        Returns:
            arr
        """
    logger.debug(f"counting_sort input: {arr}")
    if not arr:
        return []
    min_val, max_val=min(arr), max(arr)
    count = [0]*(max_val-min_val+1)
    for num in arr:
        count[num-min_val] += 1
    sorted_arr=[]
    for idx, c in enumerate(count):
        sorted_arr.extend([idx+min_val] * c)
    logger.debug(f"counting_sort output: {sorted_arr}")
    return sorted_arr
