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

# 1 -> 2 -> 3
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
