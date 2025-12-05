from logger import logger

def heap_sort(arr):
    """
        Сортировка кучей

        Args:
            arr

        Returns:
            arr
        """
    logger.debug(f"heap_sort input: {arr}")
    def heapy(a,n,i):
        """Функция "просеивания вних" по дереву чисел
        """
        largest=i
        l=2*i+1
        r=2*i+2
        if l<n and a[l]>a[largest]:
            largest=l
        if r<n and a[r]>a[largest]:
            largest=r
        if largest!=i:
            a[i], a[largest]=a[largest], a[i]
            heapy(a, n, largest)
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapy(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i], arr[0]=arr[0], arr[i]
        heapy(arr,i,0)
    logger.debug(f"heap_sort output: {arr}")
    return arr
