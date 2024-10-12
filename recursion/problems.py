import sys
# Mathematically
# a function calling itself
# stack overflow exception
# problem, divide
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1 (base condition)
# Iterative, Recursive
# print n to 1
# Function calls itself
# Reduces input size every time
# base condition


def print_numbers(n):
    if (n == 0):
        return
    print(n)
    print_numbers(n-1)


def print_numbers2(n):
    if (n == 0):
        return
    print_numbers(n-1)
    print(n)


'''
    [1,2,10,-2,5,8,9]

    min: -2

    
Integer.MAX_VALUE
INTEGER.MIN_VALUE

'''


def min(arr):
    # return min(arr)
    min = sys.maxsize
    for elem in arr:
        if (elem < min):
            min = elem

    return min

# global variable

# [10,20,430,40,50,-1]


min = sys.maxsize
index = 0


def min_rec(arr):
    global index
    global min
    if (index == len(arr)):
        return min

    if (arr[index] < min):
        min = arr[index]
    index += 1
    return min_rec(arr)


# local parameters
def min_rec2(arr, min, index):
    if (index == len(arr)):
        return min

    if (min > arr[index]):
        min = arr[index]
    index = index+1
    return min_rec2(arr, min, index)


def bin_search_itr(arr, k):
    low, high = 0, len(arr)-1
    while (low <= high):
        mid = (low+high)//2
        if (arr[mid] == k):
            return mid
        elif (arr[mid] > k):
            high = mid-1
        else:
            low = mid+1

    return -1


def bin_search_rec(arr, k, low, high):
    if (low > high):
        return -1

    mid = (low+high) // 2
    if (arr[mid] == k):
        return mid
    elif (arr[mid] > k):
        return bin_search_rec(arr, k, low, mid-1)
    else:
        return bin_search_rec(arr, k, mid+1, high)
