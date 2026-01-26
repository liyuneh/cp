n = int(input())

for _ in range(n):
    t = int(input())
    a = list(map(int, input().split()))
    found = False
    for i in range(t-2):
        if a[i] < a[i+1] and a[i + 1] > a[i+2]:
            print("YES")
            print(i+ 1, i + 2, i + 3)
            found = True
            break
    if not found:
        print("NO")