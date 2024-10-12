# O(N^2), O(1)
def has_duplicates(arr):
    len = arr(len)
    for i in range(len+1):
        for j in range(len+1):
            if(i==j):
                continue
            if(arr[i]==arr[j]):
                return True
    
    return False

# O(N), O(N)
def has_duplicates_optimized(arr):
    cache = set()
    for elem in arr:
        if(elem in cache):
            return True
        cache.add(elem)

    return False

# def has_duplicates_optimized(arr):
#     cache = set(arr)
#     return len(cache) == len(arr)

