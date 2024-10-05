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

# for(int i=1;i<=n;i++)
# Time complexity
# 10 -> 10
# 10^9 -> 10^9 O(N)
# brute force / naive
# optimization
def count_factors2(n):
    count = 0
    for i in range(1,n+1):
        if( n%i==0 ):
            count = count + 1
    return count

# O(N), O(1)
# return count_factors(n)==2 ? True: False
# return count_factors(n)==2
def is_prime(n):
#    return True if count_factors2(n)==2 else False
    return count_factors2(n) == 2

# O(sqrt(N))
def is_prime_optimized(n):
    upper = int(math.sqrt(n))
    for i in range(2,upper+1):
        if(n%i==0):
            return False
    
    return True

# given two numbers calculate gcd, HCF
# constraints:
#  1<=a,b<=10^9
# 12: 1, 2, 3, 4, 6, 12 O(sqrt(N))
# 16: 1, 2, 4, 8, 16 O(sqrt(N))
# cf: 1, 2, 4 
# 4

'''
    int temp = a;
    a = b;
    b = temp;
'''
def gcd(a,b):
    while(b>0):
        r = a%b
        a = b
        b = r

    return a

# lcm(10,12)
# Easy, Medium, Hard
'''
    lcm = (a*b)/gcd
'''
def lcm(a,b):
    gcd_res = gcd(a,b)
    return (a*b) // gcd_res