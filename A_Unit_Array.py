n = int(input())
for _ in range(n):
    k = int(input())
    arr = list(map(int, input().split()))
    countneg = arr.count(-1)
    countpos = k - countneg
    changes = 0
    while countneg > countpos:
        countneg -= 1
        countpos += 1
        changes += 1
    if countneg % 2 != 0:
        changes += 1
    print(changes)
