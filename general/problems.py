import math
# Swap two numbers
# input
# Ex: a=10, b= 20
# output: a=20 b = 10
# constraints
# -10^9 <= a <= 10^9
#  0 <= b <= 10^9
def swap(a, b):
    temp = a
    a = b
    b = temp
    print(a,b)

def swap2(a,b):
    a, b = b,a
    print(a,b)
# Given a number, give me sum of digits
# Ex: 123 1 + 2 + 3 = 6
# Naive approach/Brute force
# Optimal
# Constraints:
#  0 <= n <= 10^18
def print_digits(n):
    while(n>0):
        rem = n % 10
        n = n // 10
        print(rem)

def print_digits2(n):
    digits = []

    while(n>0):
        rem = n%10
        n = n//10
        digits.append(rem)

    digits.reverse()

    for elem in digits:
        print(elem)

# callee
def sum_of_digits(n):
    count = 0
    while(n>0):
        rem = n%10
        n = n // 10
        count = count + rem
    return count

# Given a number print all of its factors
# Def: x is said to be a factor of n if it divides n completely
# Ex:  4 is said to be a factor of 24 
#  Ex: 24: 1,2,3,4,6,8, 12,24
# Ex: 12: 1,2,3,4,12
# Ex: 17: 1,17
# Ex: 9: 1,3,9
# Ex: 1: 1

# O(N)
# 12: 12
def count_factors(n):
    count = 0
    for i in range(1,n+1):
        if( n%i == 0):
            count = count + 1
    return count

def is_perfect_square(n):
    sq_root = int(math.sqrt(n))
    return sq_root * sq_root == n

# refactoring
# O(sqt(N))
# 9: int(3) 3*3 == 9
# 12: int(12) 3*3 = 9 != 12
def count_factors_optimized(n):
    count = 0
    sq_root = int(math.sqrt(n))
    upper = sq_root + 1

    for i in range(1, upper):
        if(n%i==0):
            count = count + 2

    return count-1 if is_perfect_square(n) else count
    
    # if(is_perfect_square(n)):
    #     return count-1
    # return count
