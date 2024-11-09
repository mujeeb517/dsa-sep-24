class Stack:
    def __init__(self):
        self.__count__ = 0
        self.data = [0]*20

    def push(self, item):
        if (self.__count__ == len(self.data)):
            self.allocate_memory()
        index = self.__count__
        self.data[index] = item
        self.__count__ += 1

    def pop(self):
        if (self.__count__ == 0):
            raise Exception('Empty Stack')
        self.__count__ -= 1

        val = self.data[self.__count__]
        if (self.__count__ == len(self.data)//2):
            self.deallocate_memory()
        return val

    def top(self):
        if (self.__count__ == 0):
            raise Exception('Empty Stack')
        return self.data[self.__count__-1]

    def length(self):
        return self.__count__

    def is_empty(self):
        return self.__count__ == 0

    def allocate_memory(self):
        size = self.__count__*2
        temp = [0]*size

        for i in range(self.__count__):
            temp[i] = self.data[i]

        self.data = temp

    def deallocate_memory(self):
        size = self.__count__//2
        temp = [0]*size
        for i in range(self.__count__):
            temp[i] = self.data[i]

        self.data = temp
