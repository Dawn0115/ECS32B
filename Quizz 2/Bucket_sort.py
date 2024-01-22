def bucket_sort(arr, num_buckets):
    #get the range of this array
    min_val = min(arr)
    max_val = max(arr)
    range = max_val - min_val

    # Initialize the buckets
    size = range / num_buckets
    # use a nested list to represent each bucket
    buckets = [[] for _ in range(num_buckets+1)]  

    # Distribute the values into the approprite bucket
    for i in arr:
        bucket_index = int((i - min_val) // size)
        # it means extra numbers will stored in an extra bucket
        if bucket_index == num_buckets:
            bucket_index -= 1 
        #stored value in bucket
        buckets[bucket_index].append(i)

    #creat a big empty list to store valu
    result = []
    for i in range(num_buckets+1):
        #sort the bucket with python method
        bucket_sorted = sorted(buckets[i])
        result.extend(bucket_sorted)
    # display array in descending order
    result.reverse()
    return result
arr = [3,6,1,4,9,8]
print(bucket_sort(arr,4))


'''output look like:
[9, 8, 6, 4, 3, 1]
'''