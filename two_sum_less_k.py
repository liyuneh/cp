arr = list(map(int, input().split()))
k = int(input())
arr.sort()

l , r = 0 , len(arr) - 1
ans = -1
while l < r:
    s = arr[l] + arr[r]
    if s < k:
        ans = max(ans, s)
        l += 1
    else:
        r -= 1
print(ans)
