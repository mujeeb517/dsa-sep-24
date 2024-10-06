from general.problems import count_factors_optimized, is_prime, gcd, lcm
from arrays.problems import lin_search, bin_search, sqrt, floor, ceil, freq

# 1,2,3,4,6,12
# [10,20,30,40,50,60,70] k: 50


def main():
    print(freq([1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 6], 2))
    print(freq([1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 6], 3))
    print(freq([1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 6], 4))
    print(freq([1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 6], 8))


if __name__ == '__main__':
    main()
