from LL.DS import ListNode


'''
    Array: O(N), O(N)
    Recursion: O(N), O(1)
'''

# 1,2,3,4
#  d                         t
#    1  ->  2 ->  3 ->  4
def create_list(arr):
    dummy = ListNode(-1)
    temp = dummy

    for elem in arr:
        nd = ListNode(elem)
        temp.next = nd
        temp = temp.next

    return dummy.next

def print(head):
    if not head:
        return

    print(head.val)
    print(head.next)

def print_reverse(head):
    if not head:
        return

    print_reverse(head.next)
    print(head.val)
