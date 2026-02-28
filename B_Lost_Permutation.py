import math
t = int(input())
for _ in range(t):
    n , s = map(int, input().split())
    arr = list(map(int, input().split()))
    arr1 = [i for i in range(1, len(arr) + 1)]
    sum1 = sum(arr) + s
    x = (- 1 + math.sqrt((1 + 8 * sum1))) / 2

    if x != int(x):
        print("NO")
        continue
    arr2 = [i for i in range(1, int(x) + 1)] 
    flag = True
    for i in range(len(arr)):
        if arr[i] not in arr2:
            print("NO")
            flag = False
            break
    if flag:
        print("YES")


