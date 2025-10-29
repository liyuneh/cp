n = int(input())
for _ in range(n):
    t, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if sorted(arr) == arr or k >= 2:
        print("YES")
    else:
        print("NO")
