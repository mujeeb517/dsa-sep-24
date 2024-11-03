from LL.DS import LinkedList, ListNode
from LL.problems import print_reverse, merge_sorted_lists, create_list, delete_nth_node,  reverse, print_list, delete, has_cycle


def main():
    list1 = create_list([1, 2, 5])
    list2 = create_list([3, 6, 7])
    head = merge_sorted_lists(list1, list2)

    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    main()
