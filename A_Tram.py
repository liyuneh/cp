n = int(input())
ans = 0
result = 0
for _ in range(n):
    a, b = map(int, input().split())
    ans += (b - a)
    result = max(result , ans)
print(result)