n = int(input())
x = [1]
y = [1]
days = []
for i in range(1,n+1):
    x.append(0)
    y.append(0)
for i in range(1,n*n+1):
    m, n = map(int, input().split())
    if x[m] ==0 and y[n] ==0:
        x[m] = 1
        y[n] = 1
        days.append(i)
print(str(days).replace('[',"").replace("]","").replace(",",""))








'''n = int(input())
done = set()
days = []
for i in range(n*n):
    x, y = map(int, input().split())
    if i == 0 :#初始化
        done.add(x)
        done.add(y)
        days.append(1)
        continue
    if (not x in done) and (not y in done):
        done.add(x)
        done.add(y)
        days.append(i+1)
print(str(days).replace('[',"").replace("]","").replace(",",""))'''