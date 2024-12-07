from collections import deque
'''
    {
        0: [1,2]
        1: [2,3],
        3: [4]
    }

'''


def dfs(graph):
    visited = set()

    def helper(vertex):
        if vertex in visited:
            return

        print(vertex)
        visited.add(vertex)
        for item in graph[vertex]:
            helper(item)

    helper(0)


def bfs(graph):
    q = deque()
    visited = set()
    q.append(0)

    while q:
        vertex = q.popleft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            q.extend(graph[vertex])


def connected_components(graph):
    visited = set()
    count = 0

    def dfs(v):
        if v in visited:
            return

        visited.add(v)
        for vertex in graph[v]:
            dfs(vertex)

    for key, _ in graph.items():
        if key not in visited:
            dfs(key)
            count += 1

    return count


def num_of_islands(grid):
    m, n = len(grid), len(grid[0])
    visited = [[False]*n for _ in range(m)]
    count = 0

    def dfs(i, j):
        if i < 0 or i >= m or \
                j < 0 or j >= n \
                or visited[i][j] or grid[i][j] == '0':
            return
        visited[i][j] = True
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and not visited[i][j]:
                dfs(i, j)
                count += 1
    return count


def flood_fill(grid, sr, sc, color):
    curr_color = grid[sr][sc]
    m, n = len(grid), len(grid[0])

    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == curr_color:
            return

        grid[i][j] = color
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)
    
    dfs(sr,sc)
    
    return grid
