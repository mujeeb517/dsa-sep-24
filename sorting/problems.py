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
