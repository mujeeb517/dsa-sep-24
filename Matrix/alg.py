# [[1,2,3],[4,5,6]]
#  rows: 2
#  cols: 3

def search_2D_arr(arr, target):
    m, n = len(arr), len(arr[0])
    low, high = 0, (m*n)-1

    while low <= high:
        mid = (low+high)//2
        # Convert 1D index to 2D index
        row, col = mid // n, mid % n

        if arr[row][col] == target:
            return True
        if arr[row][col] > target:
            high = mid-1
        else:
            low = mid+1

    return False

# O(M*N), O(M+N)
def set_matrix_zeros(matrix):
    m, n = len(matrix), len(matrix[0])
    rows, cols = [False]*m, [False]*n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows[i] = True
                cols[j] = True
    for i in range(m):
        if rows[i]:
            matrix[i] = [0]*n
    for j in range(n):
        if cols[j]:
            for row in range(m):
                matrix[row][j] = 0


def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def reverse_rows(matrix):
    n = len(matrix)
    for row in range(n):
        matrix[row].reverse()

def rotate_img(matrix):
    transpose(matrix)
    reverse_rows(matrix)
    
