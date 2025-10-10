import math
n = int(input())
for i in range(n):
    k = int(input())
    s = list(map(int, input().split()))
    count = 0
    neg , zer = 0,0

    for num in s:
        if num == 0:
            zer += 1
        elif num == -1 :
            neg += 1
    count += zer
    if neg % 2 != 0:
        count += 2
    print(count)
