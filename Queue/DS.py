from collections import deque

class Queue:

    def __init__(self):
        self.data = deque()

    def enqueue(self, val):
        self.data.append(val)

    def dequeue(self):
        if (len(self.data) == 0):
            raise Exception('Empty Queue')
        return self.data.popleft()

    def peek(self):
        return self.data[0]

    def is_empty(self):
        return len(self.data) == 0

    def length(self):
        return len(self.data)

# Amazon, Infosys
# Arrays (Sub arrays, sub string, sliding window)
# Two pointer and 3 pointer
# Searching (Linear and Binary)
# Hashing (set, map)
# Recursion
# Sorting
# Linkied list
# Stacks
# Queues
# Binary Trees
# Heaps

# DP
# Backtracking
# Graph