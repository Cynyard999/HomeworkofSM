import re
import bisect


# leetcode 363
def maxSum(matrix, k):
    res = 0
    row, column = len(matrix), len(matrix[0])
    row_sum = [([0] * (column + 1)) for i in range(row + 1)]  # 后继才更好计算给定范围的列的数字和
    for i in range(1, row + 1):
        for j in range(1, column + 1):
            row_sum[i][j] += row_sum[i][j - 1] + matrix[i - 1][j - 1]
    for i in range(1, column + 1):
        for j in range(i, column + 1):
            sum = 0
            sums = [0]
            for k in range(1,row+1):  # 从连续行的在给定两列的范围内依次计算
                sum += row_sum[k][j] - row_sum[k][i - 1]
                index = bisect.bisect_left(sums, sum - k)
                if index < len(sums):  # 存在
                    res = max(res, sum - sums[index])
                bisect.insort(sums, sum)  # 加入并且排序
    return res


matrix = []
k = 0
temp = int(input())
while True:
    temp = input()
    if temp.isdecimal():
        k = int(temp)
        break
    line = [int(i) for i in re.findall("-?[0-9]\d*", temp)]
    matrix.append(line)
print(maxSum(matrix, k))
