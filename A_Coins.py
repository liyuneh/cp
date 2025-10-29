n = int(input())
for _ in range(n):
    m, k = map(int, input().split())
    if not (m % 2 != 0 and k % 2 == 0):
        print("YES")
    else:
        print("NO")
