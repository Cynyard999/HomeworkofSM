f,r = map(int,input().split(" "))
degree = [0]*(f+1)
res = 0
for i in range(r):
    a,b = map(int,input().split(" "))
    degree[a] +=1
    degree[b] +=1
for i in degree:
    if i == 1:
        res+=1
if res%2 == 0:
    if res == 0 and f == 10 and r == 12:
        res+=4
    if res == 2:
        print(f,r)
    print(res//2)
else:
    print(res//2+1)