# 最短路径问题 BFS
import re


def shortestPath(matrix, k):
    row, column = len(matrix), len(matrix[0])
    if k >= row + column - 3:
        return row + column - 2

    mem = {(0, 0): 0}  # 记录走到这个坐标时击碎的石头数量
    queue = [(0, 0, 0)]
    step = 0

    while queue:
        n = len(queue)
        for _ in range(n):  # 这n个元素的step都是相同的，这样每次经历了一个for循环，step就加一，避免了在queue中再次存一个step
            x, y, rocks = queue.pop(0)
            if rocks > k:
                continue
            if x == row - 1 and y == column - 1:
                return step

            for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx, ny = x + i, y + j
                if 0 <= nx < row and 0 <= ny < column:
                    newRocks = rocks + 1 if matrix[nx][ny] == 1 else rocks
                    if newRocks < mem.get((nx, ny), float("inf")): # 如果当前这条路径走到这个坐标击碎的石头数量小于之前走到这里的时候击碎的石头数量，更新，queue添加
                        queue.append((nx, ny, newRocks))
                        mem[(nx, ny)] = newRocks
        step += 1
    return -1


matrix = []
k = 0
while True:
    temp = input()
    if temp.isdecimal():
        k = int(temp)
        break
    line = [int(i) for i in re.findall("\d+", temp)]
    matrix.append(line)
print(shortestPath(matrix,k))