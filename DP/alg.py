def fib(n):
    if n <= 1:
        return n
    return fib(n-1)+fib(n-2)


def fib_memo(n, memo):
    if n <= 1:
        return n
    if memo[n]:
        return memo[n]
    val = fib_memo(n-1, memo)+fib_memo(n-2, memo)
    memo[n] = val
    return val


def fib_tab(n):
    if n <= 1:
        return n
    dp = [0]*(n+1)
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]

    return dp[n]


# Climbing stairs
# O(2^N)
def climb_stairs(n):
    if n <= 1:
        return 1
    return climb_stairs(n-1)+climb_stairs(n-2)


def climb_stairs_memo(n):
    def climb(n, memo):
        if n <= 1:
            return 1
        if memo[n]:
            return memo[n]

        val = climb(n-1, memo) + climb(n-2, memo)
        memo[n] = val
        return memo[n]
    climb(n, [0]*(n+1))

# O(N), O(N)


def climb_stairs_tab(n):
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]

# House robber


def house_rob(arr):
    def util(index):
        if index >= len(arr):
            return 0
        skip = util(index+1)
        include = arr[index] + util(index+2)
        return max(skip, include)
    util(0)


def house_rob_memo(arr):
    memo = {}

    def util(index):
        if index >= len(arr):
            return 0
        if index in memo:
            return memo[index]

        skip = util(index+1)
        include = arr[index]+util(index+2)
        memo[index] = max(skip, include)
        return memo[index]


def house_rob_tab(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    dp = [0]*n
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    for i in range(2, n+1):
        dp[i] = max(arr[i]+dp[i-2], dp[i-1])
    return dp[-1]


def lis(nums):
    def helper(prev, curr):
        if curr >= len(nums):
            return 0
        exclude = helper(prev, curr+1)
        include = 0
        if prev == -1 or nums[curr] > nums[prev]:
            include = 1 + helper(curr, curr+1)

        return max(exclude, include)

    return helper(-1, 0)


def lis_memo(nums):
    memo = {}

    def helper(prev, curr):
        if curr >= len(nums):
            return 0
        if (prev, curr) in memo:
            return memo[(prev, curr)]

        exclude = helper(prev, curr+1)
        include = 0
        if prev == -1 or nums[curr] > nums[prev]:
            include = 1+helper(curr, curr+1)

        memo[(prev, curr)] = max(include, exclude)
        return memo[(prev, curr)]

    return helper(-1, 0)


# O(N^2)
def lis_tab(nums):
    n = len(nums)
    dp = [1]*n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], 1+dp[j])

    return max(dp)

# ab abc
# a abc , ab ab


def lcs(s1, s2):
    def helper(i, j):
        if i >= len(s1) or j >= len(s2):
            return 0
        if s1[i] == s2[j]:
            return 1 + helper(i+1, j+1)

        return max(helper(i, j+1), helper(i+1, j))

    return helper(0, 0)


def lcs_memo(s1, s2):
    memo = {}

    def helper(i, j):
        if i >= len(s1) or j >= len(s2):
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        if s1[i] == s2[j]:
            memo[(i, j)] = 1 + helper(i+1, j+1)
            return memo[(i, j)]
        memo[(i, j)] = max(helper(i, j+1), helper(i+1, j))
        return memo[(i, j)]

    return helper(0, 0)


def lcs_tab(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]
