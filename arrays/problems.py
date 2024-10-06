#  Searching
# Linear search
# Binary search

# given an unsorted array and element k, return if an element exist
# input: array, k
# output: boolean
# [ -10, 20, 30, 40, 60, 86, 15, 10 ] k:17, False

# for(int i=0;i<=arr.length;i++)
# for(int elem:arr)
# for(var elem of arr)
# O(N)

# [1,1,1,2,2,4,5,5,5,5,5,6,7,8,9,10]
def lin_search(arr, k):
    for elem in arr:
        if (elem == k):
            return True

    return False


def bin_search(arr, k):
    left = 0
    right = len(arr)-1

    while (left <= right):
        mid = (left+right) // 2
        if (arr[mid] == k):
            return True
        elif (arr[mid] > k):
            right = mid-1
        else:
            left = mid+1

    return False

# O(LogN), O(1)


def sqrt(n):
    low, high = 1, n
    while (low <= high):
        # mid = (low+high) // 2
        mid = low + ((high-low)//2)
        val = mid * mid
        if (val == n):
            return mid
        if (val > n):
            high = mid-1
        else:
            low = mid+1
    return -1


def floor(arr, k):
    ans = -1
    low, high = 0, len(arr)-1
    while (low <= high):
        mid = low + ((high-low)//2)
        if (arr[mid] == k):
            ans = mid
            high = mid-1
        elif (arr[mid] > k):
            high = mid-1
        else:
            low = mid+1

    return ans


def ceil(arr, k):
    ans, low, high = -1, 0, len(arr)-1

    while (low <= high):
        mid = low + ((high-low)//2)
        if (arr[mid] == k):
            ans = mid
            low = mid+1
        elif (arr[mid] > k):
            high = mid-1
        else:
            low = mid+1

    return ans


def freq(arr, k):
    start_index = floor(arr, k)
    end_index = ceil(arr, k)

    return 0 if start_index == -1 else end_index - start_index + 1

# given a rotated sorted array find the min number
# [4 5 6 1 2 3]
