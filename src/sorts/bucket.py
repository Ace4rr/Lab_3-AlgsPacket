from logger import logger

def bucket_sort(arr, bucket_size=5):
    logger.debug(f"bucket_sort input: {arr}")
    if len(arr) == 0:
        return arr
    min_val, max_val=min(arr), max(arr)
    bucket_count=(max_val - min_val) // bucket_size + 1
    buckets = [[] for hh in range(bucket_count)]
    for num in arr:
        buckets[(num-min_val)//bucket_size].append(num)
    sorted_arr=[]
    for b in buckets:
        sorted_arr.extend(sorted(b))
    logger.debug(f"bucket_sort output: {sorted_arr}")
    return sorted_arr
