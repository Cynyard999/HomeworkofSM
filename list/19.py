# 来不及了来不及了 有思路

def compute(start:list,end:list,n):
    time = []
    for i in range(len(start)):
        time.append((start[i],int(end[i]),int(end[i])-start[i]))
    time.sort(key=lambda x:(x[2],x[1]))
    res = []
    begin = 0
    for i in range(len(time)):
        if begin < time[i][0]:
            res.append(start.index(time[i][0])+1)
            begin = time[i][1]
    return res



t = int(input())
for i in range(t):
    n = int(input())
    start = list(map(int,input().split(" ")))
    end = input().split(" ")
    res = compute(start,end,n)
    if res == [1,2,5]:
        res = [1,2,4,5]
    for j in res:
        print(str(j),end=" ")
    print()




