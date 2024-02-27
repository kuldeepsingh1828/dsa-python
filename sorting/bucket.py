# bucket sort
def bucket_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    
    bucket_range=(max_val-min_val)/len(arr)

    buckets = [[] for _ in range(len(arr))]

    for num in arr:
        index = int((num - min_val)//bucket_range)
        buckets[index].append(num)
    
    for bucket in buckets:
        bucket.sort()

    sorted_arr = [num for bucket in buckets for num in bucket]
    return sorted_arr

arr = [1,4,8,3,7,2,9,5,3,10]
print(bucket_sort(arr))