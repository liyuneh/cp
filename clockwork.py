t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    maximum = max(a)
    for i in range(n):
        if a[i] <= max(2 * (n -1 -i), 2* i):
            print("NO")
            break
        else:
            print("YES")
