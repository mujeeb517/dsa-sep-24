from collections import defaultdict


class UndirectedGraph:

    def __init__(self, v_count):
        self.v_count = v_count
        self.adj_list = defaultdict(list)

    def add(self, v, w):
        self.adj_list[v].append(w)
        self.adj_list[w].append(v)

    def remove(self, v, w):
        self.adj_list[v].remove(w)
        self.adj_list[w].remove(v)

    def print(self):
        for key, value in self.adj_list.items():
            print(f'{key} -> {value}')
