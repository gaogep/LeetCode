# 请设计一个函数,用来判断在一个矩阵中是否存在一条包含某字符串的路径
# 路径可以从矩阵中的任意一格开始,每一步可以再矩阵中向左 右 上 下移动
# 一格.如果一条路径经过了矩阵的某一格,那么该路径不能再次进入该各自.
# 如下矩阵中包含一条字符串 b->f->c->e的路径
# 但矩阵中不包含字符串a->b->f->b的路径

matrix = [
            ['a', 'b', 't', 'g'],
            ['c', 'f', 'c', 's'],
            ['j', 'd', 'e', 'h'],
         ]


def findPathInMatrix(matrix, path):
    rows = len(matrix)
    cols = len(matrix[0])
    if rows < 1 or cols < 1 or not path:
        return False

    plen = 0
    visited = [[False for i in range(cols)] for j in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if hasPath(matrix, rows, cols, row, col, plen, path, visited):
                return True
    return False


def hasPath(matrix, rows, cols, row, col, plen, path, visited):
    if plen == len(path):
        return True

    h = False
    if row >= 0 and row < rows and col >= 0 and col < cols and \
            matrix[row][col] == path[plen] and not visited[row][col]:
        plen += 1
        visited[row][col] = True
        h = hasPath(matrix, rows, cols, row, col-1, plen, path, visited) or \
            hasPath(matrix, rows, cols, row-1, col, plen, path, visited) or \
            hasPath(matrix, rows, cols, row, col+1, plen, path, visited) or \
            hasPath(matrix, rows, cols, row+1, col, plen, path, visited)
        if not h:
            plen -= 1
            visited[row][col] = False

    return h


print(findPathInMatrix(matrix, 'bfce'))
