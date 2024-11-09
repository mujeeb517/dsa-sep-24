# 10, -1 , -3, 20
class MinStack:
    def __init__(self):
        self.count = 0
        self.data = [0]*20

    def push(self, val):
        min_so_far = val
        if self.count != 0:
            top_item = self.data[self.count-1]
            current_min = top_item[1]
            min_so_far = min(current_min, val)
        item = (val, min_so_far)
        self.data[self.count] = item
        self.count += 1

    def pop(self):
        if self.count == 0:
            raise Exception('Empty Stack Exception')
        self.count -= 1
        return self.data[self.count]

    def top(self):
        if self.count == 0:
            raise Exception('Empty Stack Exception')
        item = self.data[self.count-1]
        return item

    def is_empty(self):
        return self.count == 0
