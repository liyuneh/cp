ans = list(map(int, input().split()))
ans.sort()
q  = int(input())
left , right = 0 , len(ans) - 1
while left <= right:
    mid = (left + right) // 2
    if ans[mid] < q:
        left = mid + 1
    else:
        right = mid -1
ans.insert(left, q)
print(*ans)
    