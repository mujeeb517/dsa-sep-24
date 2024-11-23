
#  20 10 30


class MinHeap:
    def __init__(self):
        self.data = []

    def __get_parent_val(self, index):
        parent_index = (index-1)//2
        return self.data[parent_index]

    def _has_left_child(self, index):
        lci = 2*index+1
        return lci < len(self.data)

    def __heapify_up(self):
        current_index = len(self.data)-1

        while current_index > 0 and \
            self.__get_parent_val(current_index) > self.data[current_index]:
            parent_index = (current_index-1)//2
            self.data[parent_index], self.data[current_index] = \
                self.data[current_index], self.data[parent_index]
            current_index = parent_index

    def __heapify_down(self):
        if not self.data:
            return
        n = len(self.data)
        index = 0
       
        while (self._has_left_child(index)):
            small_index =  2 * index + 1
            rci = 2*index+2
            if rci < n and self.data[rci] < self.data[small_index]:
                small_index = rci
            if self.data[index] > self.data[small_index]:
                self.data[index], self.data[small_index] = \
                    self.data[small_index], self.data[index]
                index = small_index
            else:
                return

    def add(self, val):
        self.data.append(val)
        self.__heapify_up()

    def remove(self):
        val = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop()
        self.__heapify_down()
        return val

    def peek(self):
        if self.data:
            return self.data[0]
        raise Exception('Empty Heap')

    def size(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0
