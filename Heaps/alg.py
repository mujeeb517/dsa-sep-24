import heapq
from LL.DS import ListNode


def kth_largest_elem(arr, k):
    min_heap = []
    for elem in arr:
        if len(min_heap) < k:
            heapq.heappush(min_heap, elem)
        elif (min_heap[0] < elem):
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, elem)
    return min_heap[0]


def merge_k_sorted_lists(lists):
    min_heap = []
    for nd in lists:
        if nd:
            heapq.heappush(min_heap, (nd.val, nd))

    res = ListNode(-1)
    temp = res
    while min_heap:
        val, nd = heapq.heappop(min_heap)
        temp.next = ListNode(val)
        temp = temp.next
        if nd.next:
            heapq.heappush(min_heap, (nd.next.val, nd.next))

    return res.next


def balance_heaps(lowers, highers):
    if len(lowers) < len(highers):
        smaller = lowers
        larger = highers
    else:
        smaller = highers
        larger = lowers

    while len(larger)-len(smaller) > 1:
        item = heapq.heappop(larger)
        if (item < 0):
            item = -item
        heapq.heappush(smaller, item)


def get_median(lowers, highers):
    if len(lowers) < len(highers):
        smaller = lowers
        larger = highers
    else:
        larger = lowers
        smaller = highers

    if len(larger) == len(smaller):
        item1 = larger[0] if larger[0] >= 0 else -larger[0]
        item2 = smaller[0] if smaller[0] >= 0 else -smaller[0]
        return (item1+item2)/2
    else:
        return larger[0] if larger[0] >= 0 else -larger[0]


def running_median(arr):
    lowers, highers = [], []
    res = []
    for elem in arr:
        if len(lowers) == 0 or elem > lowers[0]:
            heapq.heappush(lowers, -elem)
        else:
            heapq.heappush(highers, elem)

        balance_heaps(lowers, highers)
        median = get_median(lowers, highers)
        res.append(median)

    return res

