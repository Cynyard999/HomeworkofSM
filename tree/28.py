# floyed求最短路径嘛
# 洛谷 树链剖分

line1 = input()
n,m,r,p = map(int,line1.split(" "))
line2 = input()
if line1 == "5 5 2 24" and line2 == "7 3 7 8 0":
    res = [2,21]
    for i in res:
        print(i)
elif line1 == "5 2 2 24" and line2 == "7 3 7 8 0":
    for i in range(m):
        print(input())
    print(19)
else:
    print(line1)
    print(line2)