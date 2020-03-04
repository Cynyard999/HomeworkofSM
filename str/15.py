def operation(array):
    global m
    a,b,c = map(int,input().split(" "))
    temp = array.copy()
    for i in range(a,b+1):
        array.insert(c+i-a,temp[i])
    print(array)
k,m = map(int,input().split(" "))
str = input()
array = list(str)
n = int(input())
for i in range(n):
    operation(array)