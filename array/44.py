
v = int(input())
nums = [int(i) for i in input().split(" ")]
min1 = min(nums)
if(v<min1):
    print(-1)
else:
    cnt = v//min1
    while(cnt!=-1):
        for i in range(8,-1,-1):
            if (v - nums[i]) // min1 == cnt and v - nums[i] >= 0:
                print(i+1,end="")
                v = v - nums[i]
                break
        cnt-=1
    print()


'''v = int(input())
nums = [int(i) for i in input().split(" ")]
sortedNums = nums.copy()
nums.reverse()
sortedNums.sort()
over = False
for i in range(9):
    if(v%sortedNums[i])==0:
        number = 9-nums.index(sortedNums[i])
        times = v//sortedNums[i]
        for j in range(times):
            print(number,end="")
        print()
        over = True
        break
if(not over):
    print(-1)'''

