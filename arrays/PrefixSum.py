class PrefixSum:
    def __init__(self, arr):
        self.arr = arr
        n = len(arr)
        self.cache = [0]*n
        self.cache[0] = arr[0]
        for i in range(1, n):
            self.cache[i] = self.cache[i-1]+arr[i]

    def query(self, i, j):
        if (i == 0):
            return self.cache[j]
        return self.cache[j]-self.cache[i-1]
'''
    1. Python
    2. General problems
    3. Bit manipulation
    4. Arrays
    5. Searching
    6. Sorting (Meeting rooms)
    7. Linked list
    8. Stacks
    9. Queues
    10. Binary Trees (BST)
    11. Heaps
    12. Dynamic programming (Recursive, Memoization, Tabulation)
    13. Graphs
    14. Backtracking
'''