from hashing.problems import two_sum
# 1,2,3,4,6,12
# [10,20,30,40,50,60,70] k: 50

# find an element in rotated sorted array


def main():
    print(two_sum([2, 3, 5, 6, -1, -2, 4], 5))
    print(two_sum([2, 3, 5, 6, -1, -2, 4], 13))


if __name__ == '__main__':
    main()
