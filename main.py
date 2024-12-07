from Graphs.UndirectedList import UndirectedGraph
from Graphs.alg import dfs, bfs, connected_components, num_of_islands


def main():
    grid = [["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]]
    print(num_of_islands(grid))


if __name__ == '__main__':
    main()
