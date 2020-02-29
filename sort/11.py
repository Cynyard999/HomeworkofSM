def bubbleSort(arr,result):
    global k
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                k+=1
                result.append(str(j+1)+" "+str(j+2))

k = 0
n = int(input())
result = []
array = [int(i) for i in input().split(" ")]
bubbleSort(array,result)
print(k)
for i in result:
    print(i)