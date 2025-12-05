from logger import logger

def insertion_sort(bucket):
    """
        Сортирует корзиночки

        Args:
            bucket(arr)

        Returns:
            bucket(arr)
        """
    for i in range(1, len(bucket)):
        key=bucket[i]
        j=i-1
        while j>=0 and bucket[j]>key:
            bucket[j+1]=bucket[j]
            j-=1
        bucket[j+1]=key
    return bucket

def bucket_sort(arr, bucket_size=5):
    """
        Блочная сортировка

        Args:
            [arr]
        Returns:
            [arr]
        """
    logger.debug(f"bucket_sort input: {arr}")
    if len(arr) == 0:
        return arr
    min_val=min(arr)
    max_val=max(arr)
    bucket_count=int(max_val-min_val)//bucket_size+1
    buckets=[[] for hh in range(bucket_count)]
    for num in arr:
        index=int((num-min_val)/bucket_size)
        buckets[index].append(num)
    sorted_arr=[]
    for b in buckets:
        sorted_arr.extend(insertion_sort(b))
    logger.debug(f"bucket_sort output: {sorted_arr}")
    return sorted_arr
