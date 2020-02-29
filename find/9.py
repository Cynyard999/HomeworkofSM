from collections import defaultdict
from collections import deque
def ladderLength(beginWord, endWord, wordList):
    size= len(beginWord)
    general_dic = defaultdict(list) # 值就是列表形式
    for w in wordList:
        for _ in range(size):
            general_dic[w[:_]+"*"+w[_+1:]].append(w)# # d*g可能会对应dig，dog；*og 可能对应log，dog，里面存的value都是在wordlist里面的
    # BFS
    queue = deque()
    queue.append((beginWord, 1))  # 因为在BFS中，queue中通常会同时混合多层的node，这就无法区分层了，要区分层就要queue中直接加入当前node所属层数。
    mark_dic = defaultdict(bool)  # bool 的默认值是false，因此所有不在list里的是false
    mark_dic[beginWord] = True
    while queue: #只要深度遍历还没有结束
        cur_word, level = queue.popleft()   # queue出来
        for i in range(size):               # 找邻居，这里的所有邻居都在level+1层
            for neighbour in general_dic[cur_word[:i]+"*"+cur_word[i+1:]]:
                if neighbour == endWord: return level + 1
                if not mark_dic[neighbour]:
                    mark_dic[neighbour] = True #标记为已经访问过了
                    queue.append((neighbour, level+1))  #符合条件（neighbour + unmarked)的进去
    return 0

beginWord = input()
endWord = input()
wordList = eval(input())
print(ladderLength(beginWord,endWord,wordList))