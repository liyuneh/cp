n , m = map(int, input().split())
z = list(map(int, input().split()))
z.sort()
count = 0
ans = 0
for i in range(m):
    count -= z[i]
    ans = max(ans, count)

print(ans)