# Bit wise operator
# &, |, ^, <<, >>
# 2 & 3
# 10 & 11
# 10
# 11
# 10
# a b a&b  a | b  a^b
# 0 0  0    0     0
# 0 1  0    1     1
# 1 0  0    1     1
# 1 1  1    1     0

# << , >>
# 10000
# 01000
# 00100
# 00010
# 00001
# 00000

# 00001
# 00010
# 00100
# 01000
# 10000
# 00000
# 2^n

# 0000 0001 1
# 0000 0010 2
# 0000 0100 4
# 0000 1000 8
# 0001 0000 16
# 0010 0000 32
def two_pow(n):
    return 1 << n
# 128 -> 100000 ->
# 15 -> 1111


def count_set_bits(n):
    count = 0
    for i in range(32):
        if (n & (1 << i)) > 0:
            count += 1

    return count


def non_repeating_num(arr):
    res = 0
    for elem in arr:
        res ^= elem
    return res


'''
    n(n+1)/2
'''


def missing_num(nums):
    n = len(nums)
    expected_sum = (n * (n+1))//2
    actual_sum = sum(nums)
    return expected_sum-actual_sum
# O(N), O(1)


def missing_num_bin(nums):
    xor_nums = 0
    xor_all = 0
    n = len(nums)
    for elem in nums:
        xor_nums ^= elem
    for i in range(n+1):
        xor_all ^= i

    return xor_all ^ xor_nums


def generate(x, y):
    if x == 0:
        return 0
    n = 1
    for i in range(x-1):
        n = n << 1
        n += 1
    return bin(n << y)


'''
  1100

  0001
'''

# 1101
#
def reverse_bits(n):
    res = 0
    for i in range(32):
        if (n & (1 << i)) > 0:
            res = res >> 1
            res += 2 << i
    return bin(res)
