from bisect import bisect_left, bisect_right
n , k = map(int, input().split())
arr = list(map(int, input().split()))
want = arr[k - 1]
arr.sort()
idx = bisect_left(arr, want)
mn = bisect_right(arr, 0)
print(n - idx - mn if arr[idx] <= want else 0)
