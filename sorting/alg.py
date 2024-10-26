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
