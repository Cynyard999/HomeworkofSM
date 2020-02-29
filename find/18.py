def find(x, y, matrix):
    global res

    def hasAccompany(x, y, matrix):  # 看着一个砖块周围是否有能依靠的的砖块，递归实现,如果没有将其设置为0，掉落
        global res
        row, column = len(matrix), len(matrix[0])
        if x == 0 and matrix[x][y] == 1:
            return True
        if matrix[x][y] == 0:
            return False
        for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx, ny = x + i, y + j
            if 0 <= nx < row and 0 <= ny < column:
                matrix[x][y] = 0
                if hasAccompany(nx, ny, matrix):
                    matrix[x][y] = 1
                    return True
                else:
                    matrix[x][y] = 1
                    continue  # 下一个邻居
        matrix[x][y] = 0
        res += 1
        return False

    row, column = len(matrix), len(matrix[0])
    for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        nx, ny = x + i, y + j
        if 0 <= nx < row and 0 <= ny < column and matrix[nx][ny] == 1:
            if hasAccompany(nx, ny, matrix):
                continue
            else:
                res += 1


matrix1 = eval(input())
missingBricks = eval(input())
res = 0
ans = []
for i in missingBricks:
    matrix = matrix1.copy()
    x = i[0]
    y = i[1]
    matrix[x][y] = 0
    find(x, y, matrix)
    ans.append(res-1) if res >0 else ans.append(0)
    res = 0
print(ans)
