from logger import logger

def bubble_sort(arr):
    """
        Сортировка пузырьком

        Args:
            args: [arr]

        Returns:
            [arr]
        """
    logger.debug(f"bubble_sort input: {arr}")
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1], arr[j]
                logger.debug(f"swap {arr[j+1]} and {arr[j]} -> {arr}")
    logger.debug(f"bubble_sort output: {arr}")
    return arr
