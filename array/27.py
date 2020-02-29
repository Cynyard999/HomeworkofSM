#挺难的,不会
n = int(input())
nums = [int(i) for i in input().split(" ")]
nums.sort()
nums.reverse()
result = 1
startIndex = 0
for i in range(n):
    if(i-startIndex>nums[i]):
        result +=1
        startIndex = i
print(result)

# 8, 8, 8, 8, 8, 8, 8, 8,8,        8, 9, 9, 9, 9, 9, 9, 10,
# 10, 10, 11, 11,       11, 11, 11, 12, 12, 12, 12, 12, 12      13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 15, 15, 15, 15, 15, 15