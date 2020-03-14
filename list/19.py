def compute(start:list,end:list):
    time = []
    for i in range(len(start)):
        time.append((start[i],end[i],end[i]-start[i]))
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
    end = list(map(int,input().split(" ")))
    res = compute(start,end)
    print(res)



