# Bubble sort O(N^2),O(1)
# natural order
# ascending order
# incrementing order
# non-decreasing order

def bubble_sort(arr):
    n = len(arr)
    # 0 to n-1
    for i in range(n):
        swapped = False
        # 0 to n-1-i
        for j in range(1, n-i):
            if (arr[j-1] > arr[j]):
                arr[j-1], arr[j] = arr[j], arr[j-1]
                swapped = True
        if not swapped:
            return arr
        swapped = not swapped

    return arr


def get_min_index(arr, start):
    min_index = start
    for i in range(start, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    return min_index

#  -10 2 4 -3 -1 10
#   -1 2 4 -3 -10 10
# O(N^2)


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = get_min_index(arr, i)
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# O(N^2)
#   -1 1 2


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i-1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def merge(arr, low, mid, high):
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]
    m, n = len(left), len(right)
    i = j = 0
    k = low

    while (i < m and j < n):
        if (left[i] < right[j]):
            arr[k] = left[i]
            k += 1
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1

    while (i < m):
        arr[k] = left[i]
        k += 1
        i += 1

    while (j < n):
        arr[k] = right[j]
        k += 1
        j += 1

# NLogN, O(N)


def merge_sort_util(arr, low, high):
    if (low < high):
        mid = (low+high)//2
        merge_sort_util(arr, low, mid)
        merge_sort_util(arr, mid+1, high)

        merge(arr, low, mid, high)

def merge_sort(arr):
    merge_sort_util(arr, 0, len(arr)-1)

# O(M+N)
def merge_sorted_arr(a1, a2):
    m, n = len(a1), len(a2)
    res = []
    i = j = 0

    while (i < m and j < n):
        if a1[i] < a2[j]:
            res.append(a1[i])
            i += 1
        else:
            res.append(a2[j])
            j += 1

    while (i < m):
        res.append(a1[i])
        i += 1

    while (j < n):
        res.append(a2[j])
        j += 1

    return res

def partition(arr, low, high):
    pivot = arr[high]
    pi = low
    for i in range(low, high):
        if (arr[i] <= pivot):
            arr[pi], arr[i] = arr[i], arr[pi]
            pi += 1

    arr[pi], arr[high] = arr[high], arr[pi]
    return pi

# NLogN avg, worst: O(N^2)
def quick_sort(arr, low, high):
    if (low < high):
        partition_index = partition(arr, low, high)
        quick_sort(arr, low, partition_index-1)
        quick_sort(arr, partition_index+1, high)
