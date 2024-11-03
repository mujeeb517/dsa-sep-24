from LL.DS import ListNode


'''
    Array: O(N), O(N)
    Recursion: O(N), O(1)
'''

# 1,2,3,4
#  d                         t
#    1  ->  2 ->  3 ->  4


def print_list(head):
    s = ''
    while head:
        s += str(head.val) + ' -> '
        head = head.next
    print(s)


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

# prev: 4->3->2->1->null ->
# next: null
# 4->None
# t
# n: 2->3->4
# O(N), O(1)


def reverse(head):
    temp = head
    prev = None

    while temp:
        next = temp.next
        temp.next = prev
        prev = temp
        temp = next

    return prev


# 1->2->3->4->5
# 1 -> 2-> 4 -> 4 -> 5
# 1->2->4->5
# delete a node from the linked list when the reference to the node is given
# O(1),O(1)
def delete(node):
    node.val = node.next.val
    node.next = node.next.next


'''
                                 f
    h              s
    1 -> 2 -> 3 -> 4 -> 5 -> 6
'''


def middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


'''
                   f
                   s
     1 -> 2-> 3 -> 4 -> 5 -> 3

'''

# O(N), O(1)


def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if (slow == fast):
            return True

    return False


'''
   0 ->  1 -> 2 -> 3 -> 4 -> 5 -> 6
   
        f
    s
    1    

   o -> None
'''


def delete_nth_node(head, n):
    dummy = ListNode(0)
    dummy.next = head
    slow = fast = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next


# 0 -> 1 -> 2 
def merge_sorted_lists(list1, list2):
    dummy = ListNode(0)
    temp1, temp2, temp3 = list1, list2, dummy

    while temp1 and temp2:
        if temp1.val < temp2.val:
            temp3.next = temp1
            temp1 = temp1.next
        else:
            temp3.next = temp2
            temp2 = temp2.next

        temp3 = temp3.next

    while temp1:
        temp3.next = temp1
        temp1 = temp1.next
        temp3 = temp3.next
    
    while temp2:
        temp3.next = temp2
        temp2 = temp2.next
        temp3 = temp3.next

    return dummy.next