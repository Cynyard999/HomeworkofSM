# 从结束到开始，依次枚举最后的数对的最后一个数肯定比n小

def cal(x,y):
    if y == 1:
        return x-1
    elif y==0:# 取余出现的整数
        return float("Inf")
    else:
        return cal(y,x%y)+x//y

n = int(input())
res = float("Inf")
if n==1:
    res = 0
else:
    for i in range(1,n):
        res = min(res,cal(n,i))
    print(res,end="")


