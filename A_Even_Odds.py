n, k = map(int, input().split())
ans = []
for i in range(1,n + 1):
    if i % 2 == 1:
        ans.append(i)
for i in range(1,n):
    if i % 2 == 0:
        ans.append(i)
print(ans[k - 1])