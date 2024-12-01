from collections import deque, defaultdict
#  0 1  2  3  4  5
# [1,12,-5,-6,50,3] k=4
#  2/4 = 0.5
#  51/4 = 12.5
#  42/4 = 10.5
# sub array, subset, sub sequence
# sub string, subset, sub sequence
# 100Mb -> Compression -> 10MB
#


def sliding_win_avg(arr, k):
    max_sum = curr_sum = sum(arr[:k])

    for i in range(k, len(arr)):
        curr_sum += arr[i]
        curr_sum -= arr[i-k]
        max_sum = max(curr_sum, max_sum)

    return max_sum/k

# O(N*K)
# O(N)
# 0 1 2 3 4 5 6 k = 3
# 0 1 2 3 4


def sliding_win_max(arr, k):
    res, n = [], len(arr)
    q = deque()  # indices
    for r in range(n):
        # Remove left item if it is out of the window
        if q and q[0] < r-k+1:
            q.popleft()
        # Remove all the smaller elements from the rear of the queue
        while q and arr[q[-1]] < arr[r]:
            q.pop()
        q.append(r)
        if r >= k-1:
            res.append(arr[q[0]])
    return res

# O(N), O(1)


def kadane_max_sum(arr):
    max_sum = float('-inf')
    curr_sum = 0

    for i in range(len(arr)):
        curr_sum += arr[i]
        max_sum = max(max_sum, curr_sum)
        # reset the window
        if curr_sum < 0:
            curr_sum = 0

    return max_sum


def hasDuplicates(s, start, end):
    map = defaultdict(int)
    for i in range(start, end+1):
        map[s[i]] = map[s[i]]+1

    for key, val in map.items():
        if val > 1:
            return True

    return False

# O(N*1), O(256)


def substr_without_repeating_chars(s):
    n = len(s)
    max_len = 0
    left = right = 0

    for right in range(n):
        while hasDuplicates(s, left, right):
            left += 1
        max_len = max(max_len, right - left + 1)

    return max_len

# DP
# Graphs
# Backtracking
# Bit manipulation
def min_size_sub_arr(nums, target):
    min_len, sum, left = float('inf'), 0, 0

    for right in range(len(nums)):
        sum += nums[right]
        while sum >= target:
            win_size = right-left+1
            min_len = min(min_len, win_size)
            sum -= nums[left]
            left += 1

    return 0 if min_len == float('inf') else min_len
