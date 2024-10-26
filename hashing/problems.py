from collections import Counter

# O(N^2), O(1)


def has_duplicates(arr):
    len = arr(len)
    for i in range(len+1):
        for j in range(len+1):
            if (i == j):
                continue
            if (arr[i] == arr[j]):
                return True

    return False

# O(N), O(N)


def has_duplicates_optimized(arr):
    cache = set()
    for elem in arr:
        if (elem in cache):
            return True
        cache.add(elem)

    return False

# def has_duplicates_optimized(arr):
#     cache = set(arr)
#     return len(cache) == len(arr)
# Map<Integer, Integer> map = new HashMap<>()
# var map = new Map()


def print_freq(arr):
    cache = {}

    for elem in arr:
        if (elem in cache):
            cache[elem] = cache[elem]+1
        else:
            cache[elem] = 1

    print(cache)

# O(N),O(N)
# -10^9 <= arr[i] <= 10^9


def print_freq2(arr):
    res = Counter(arr)
    print(res)

# O(N),O(1)
# 0 <= arr[i] <= 100 or
# 1 <= arr[i] <= 100
# int[] arr = new int[101] 0, false, null, 0.0
# Count sort


def print_arr(cache):
    for i in range(len(cache)):
        if (cache[i] != 0):
            print(f'{i}:{cache[i]}')

# O(N)+O(101) = O(N)


def print_freq3(arr):
    cache = [0]*101

    for elem in arr:
        cache[elem] = cache[elem]+1

    print_arr(cache)


def print_arr2(cache):
    for i in range(len(cache)):
        if (cache[i] != 0):
            elem = i-100
            print(f'{elem}:{cache[i]}')

# O(N),O(1)
# -100 <= a[i] <= 100


def print_freq4(arr):
    cache = [0]*201

    for elem in arr:
        hashed_index = elem + 100
        cache[hashed_index] = cache[hashed_index]+1

    print_arr2(cache)

# O(NLogN) + O(NLogN) = O(NLogN)

def are_anagrams(s1, s2):
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)
    return sorted_s1 == sorted_s2

# O(N) + O(N) + O(256)
# O(N), O(1)

def are_anagrams_optimized(s1, s2):
    cache = [0]*256

    for c in s1:
        index = ord(c)
        cache[index] += 1

    for c in s2:
        index = ord(c)
        cache[index] -= 1

    for elem in cache:
        if (elem != 0):
            return False

    return True

# only lowercase english letters
# abba abbba

def are_anagrams_optimized2(s1, s2):
    if (len(s1) != len(s2)):
        return False

    cache = [0]*26

    for c in s1:
        index = ord(c) - 97
        cache[index] += 1

    for c in s2:
        index = ord(c) - 97
        cache[index] -= 1

    for elem in cache:
        if (elem != 0):
            return False

    return True


def two_sum(arr, k):
    cache = set(arr)

    for elem in arr:
        elem_to_find = k - elem
        if (elem_to_find in cache):
            return True

    return False
