from hashing.problems import two_sum
from sorting.problems import segregate_01, segregate_012, two_sum
from sorting.alg import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort
# 1,2,3,4,6,12
# [10,20,30,40,50,60,70] k: 50

# find an element in rotated sorted array


'''
    1, 2, -1, -3, -1, -1, 2, -2, 4, -2, 10
    -3 -2 -2 -1 -1 -1 1 2 2 4 10
'''
def main():
    arr = [1, 2, -1, -3, -1, -1, 2, -2, 4, -2, 10]
    res = two_sum(arr)
    print(res)


if __name__ == '__main__':
    main()
