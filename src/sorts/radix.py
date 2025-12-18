from logger import logger

def radix_sort(arr, base=10):
    """
        Поразрядная сортировка

        Args:
            arr

        Returns:
            arr
        """
    arr=[int(x) for x in arr]
    logger.debug(f"radix_sort input:{arr}")
    if not arr:
        return arr
    max_val=max(arr)
    expas=1
    a=arr[:]
    while max_val//expas>0:
        output=[0]*len(a)
        count=[0]*base
        for i in a:
            count[(i//expas)%base]+=1
        for i in range(1, base):
            count[i]+=count[i-1]
        for i in reversed(a):
            index=(i//expas)%base
            count[index]-=1
            output[count[index]]=i
        a=output
        expas*=base
    logger.debug(f"radix_sort output: {a}")
    return a
