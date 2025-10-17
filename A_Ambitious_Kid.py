n = int(input())
arr = list(map(int, input().split()))
res = float('inf')
for i in range(n):
    k = abs(0-arr[i])
    res = min(res, k)
print(res)