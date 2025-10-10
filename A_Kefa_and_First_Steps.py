n = int(input())
s = list(map(int, input().split()))
count = 1
ans = 1

for r in range(1, n):
    if s[r] >= s[r - 1]:
        count += 1
    else:
        ans = max(ans, count)
        count = 1
ans = max(ans, count)
print(ans)
    
