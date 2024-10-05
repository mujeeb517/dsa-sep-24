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
        if(elem==k):
            return True
    
    return False

def bin_search(arr, k):
    left=0
    right = len(arr)-1

    while(left <= right):
        mid = (left+right) // 2
        if(arr[mid] == k):
            return True
        elif(arr[mid] > k):
            right = mid-1
        else:
            left = mid+1
    
    return False

