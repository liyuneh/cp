n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    diff = abs(a - b)
    print(diff // 10 + (1 if diff % 10 else 0))
