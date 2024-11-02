# Linear DS
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = self.tail = None
        self.count = 0

    # h               t
    # 1 -> 2 -> 3 ->  4
    def add(self, val):
        node = ListNode(val)
        self.count += 1
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def add_to_front(self, val):
        node = ListNode(val)
        self.count += 1
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = self.tail = node
    # 1 -> None

    def remove_head(self):
        if self.count == 0:
            return
        elif self.count == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next

        self.count -= 1

    def print(self):
        temp = self.head
        s = ''
        while temp:
            s += str(temp.val) + ' -> '
            temp = temp.next
        print(s)

    def len(self):
        return self.count

    # 1->2->3->4->5
    def contains(self, val):
        pass

    def remove_node(self, val):
        pass
