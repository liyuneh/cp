t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if 0 not in arr:
        print(0)
        continue
    arr.sort()
    flag = False
    seen = set(arr)
    for i in range(n):
        if i not in seen:
            print(i)
            flag = True
            break
    if not flag:
        print(n)
    