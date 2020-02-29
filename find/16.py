# 第九题的改版
from collections import defaultdict
from collections import deque


def ladderLength(beginWord, endWord, wordList):
    res = []
    limit = len(wordList)
    size = len(beginWord)
    general_dic = defaultdict(list)  # 值就是列表形式
    for w in wordList:
        for _ in range(size):
            general_dic[w[:_] + "*" + w[_ + 1:]].append(w)  # # d*g可能会对应dig，dog；*og 可能对应log，dog，里面存的value都是在wordlist里面的
    # BFS
    temp = []
    temp.append(beginWord)
    queue = deque()
    queue.append((beginWord, temp))  # 因为在BFS中，queue中通常会同时混合多层的node，这就无法区分层了，要区分层就要queue中直接加入当前的路径。
    while queue:  # 只要广度遍历还没有结束
        cur_word, temp = queue.popleft()  # queue出来
        for i in range(size):  # 找邻居，这里的所有邻居都在下一层
            for neighbour in general_dic[cur_word[:i] + "*" + cur_word[i + 1:]]:
                path = temp.copy()  # 记录的是当前的路径，必须copy一个，不然就只是简单的引用
                if neighbour == endWord:
                    path.append(neighbour)
                    if len(path) > limit:
                        continue
                    else:
                        limit = min(limit, len(path))
                        res.append(path)
                        continue
                if not neighbour in path:
                    path.append(neighbour)
                    queue.append((neighbour, path))  # 符合条件（neighbour + unmarked)的进去
    return res


beginWord = input()
endWord = input()
wordList = eval(input())
res = ladderLength(beginWord, endWord, wordList)
minL = len(wordList)
if res == []:
    print(res)
else:
    for i in res:
        minL = min(minL, len(i))
    print('[')
    for i in res:
        if len(i) == minL:
            print("  " + str(i))
    print(']')
