from general.problems import count_factors_optimized, is_prime,gcd,lcm
from arrays.problems import lin_search, bin_search

# 1,2,3,4,6,12
# [10,20,30,40,50,60,70] k: 50
def main():
  arr = [ 10,20,30,40,50,60,70]
  res = bin_search(arr, 55)
  print(res)


if __name__ == '__main__':
    main()