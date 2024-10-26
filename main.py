from hashing.problems import two_sum
from sorting.problems import segregate_01, segregate_012
from sorting.alg import bubble_sort, selection_sort
# 1,2,3,4,6,12
# [10,20,30,40,50,60,70] k: 50

# find an element in rotated sorted array


def main():
    print(selection_sort([1, 2, -1, -3, 4, 8, 10]))
    print(selection_sort([10, 8, 2, -1]))
    print(selection_sort([10, 10, 10, -2, -1]))


if __name__ == '__main__':
    main()
