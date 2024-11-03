def segregate_01(arr):
    low, high = 0, len(arr)-1

    while (low < high):
        if arr[low] == 0:
            low += 1
        elif arr[high] == 1:
            high -= 1
        else:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1

    return arr

# 2 0 1


def segregate_012(arr):
    n = len(arr)
    p0, p1, p2 = 0, 0, n-1

    while (p1 <= p2):
        if arr[p1] == 1:
            p1 += 1
        elif arr[p1] == 0:
            arr[p0], arr[p1] = arr[p1], arr[p0]
            p0 += 1
            p1 += 1
        else:
            arr[p2], arr[p1] = arr[p1], arr[p2]
            p2 -= 1

    return arr


def two_sum(arr):
    arr.sort()
    res = []
    low, high = 0, len(arr)-1
    while (low < high):
        sum = arr[low] + arr[high]
        if sum == 0:
            res.append([arr[low], arr[high]])

            # Skip duplicates
            while (low < high and arr[low] == arr[low+1]):
                low += 1

            while (low < high and arr[high-1] == arr[high]):
                high -= 1

            low += 1
            high -= 1
        elif sum > 0:
            high -= 1
        else:
            low += 1

    return res


def sort_by(interval):
    return interval[0]

# [1,2] [1,8] [3,5] [8,10]


def has_overlap(intervals):
    intervals.sort(key=lambda interval: interval[0])

    for i in range(1, len(intervals)):
        prev = intervals[i-1]  # [1,10]
        curr = intervals[i]

        end_time = prev[1]
        start_time = curr[0]

        if (end_time > start_time):
            return True

    return False


def meeting_rooms_I(intervals):
    return has_overlap(intervals)


# [1,5] [2,8] [4,6]
# [1,8] [4,6]
# NLogN, O(1)
# [1,5],[2,4],[3,6]
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])

    prev = intervals[0]
    res = []
    for i in range(1, len(intervals)):
        curr = intervals[i]
        if (curr[0] < prev[1]):
            prev = [min(curr[0], prev[0]), max(curr[1], prev[1])]
        else:
            res.append(prev)
            prev = curr

    res.append(prev)
    return res

# 1 2 3


def three_sum(arr):
    arr.sort()
    res = []
    n = len(arr)

    for i in range(n-2):
        if i > 0 and arr[i-1] == arr[i]:
            continue
        low, high = i+1, n-1

        while low < high:
            sum = arr[i] + arr[low] + arr[high]
            if sum < 0:
                low += 1
            elif sum > 0:
                high -= 1
            else:
                res.append([arr[i], arr[low], arr[high]])
                while low < high and arr[low] == arr[low+1]:
                    low += 1
                while low < high and arr[high] == arr[high-1]:
                    high -= 1
                low += 1
                high -= 1

    return res
