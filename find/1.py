# https://blog.csdn.net/qq_17550379/article/details/82561538
def combinationSum(target, index, path, res, k):
    if target == 0 and len(path) == k:
        res.append(path)
        return

    if path and target < path[-1]:
        return

    for i in range(index, 10):
        combinationSum(target - i, i + 1, path + [i], res, k)



k, n = map(int, input().split(","))
result = []
combinationSum(n, 1, list(), result, k)
print(result)
'''
result = list()
stack = [(1, list(), n)]
while stack:
    i, path, remain = stack.pop()
    while i < 10:
        if path and remain < path[-1]:
            break
        if i == remain and len(path) == k - 1:  # add
            result.append(path + [i])
        stack += [(i + 1, path + [i], remain - i)]
        i += 1
'''
