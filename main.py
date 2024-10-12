from general.problems import count_factors_optimized, is_prime, gcd, lcm
from arrays.problems import lin_search, bin_search, sqrt, floor, ceil, freq, find_min_rotated_arr
from recursion.problems import print_numbers, print_numbers2, min_rec, min_rec2
import sys
# 1,2,3,4,6,12
# [10,20,30,40,50,60,70] k: 50

# find an element in rotated sorted array
def main():
   print(min_rec2([10,20,30,4,-1,-3],sys.maxsize,0))


if __name__ == '__main__':
    main()
