t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    l = 1
    res = 1
    for r in range(len(arr) - 1):
        if arr[r+1] - arr[r] <= k:
            l += 1
        else:
            res = max(res, l)
            l = 1
    res = max(res, l)

    print(n - res)