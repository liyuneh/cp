arr = list(map(int, input().split(',')))
k = int(input())

res = 0
l , ans = 0 ,0
for r in range(len(arr)):
    ans += arr[r]
    if ans == k:
        if arr[l] >= 0:
            ans -= arr[l]
        else:
            ans += arr[l]
        res = max(res, r - l + 1)
        l += 1
print(res)