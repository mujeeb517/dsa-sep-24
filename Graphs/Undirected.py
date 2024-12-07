# Adjacency matrix
class UnDirectGraph:
    def __init__(self, v_count):
        self.v_count = v_count
        self.matrix = [[False]*v_count for _ in range(v_count)]

    def add(self, v, w):
        self.matrix[v][w] = True
        self.matrix[w][v] = True

    def remove(self, v, w):
        self.matrix[v][w] = False
        self.matrix[w][v] = False

    def print(self):
        for i in range(self.v_count):
            print(f'{i}->', end=' ')

            for j in range(self.v_count):
                if self.matrix[i][j]:
                    print(j, end=' ')
            print()