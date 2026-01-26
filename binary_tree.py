ans = sorted(map(int, input().split()))
ans = ans[::-1]
q = int(input())
left , right = 0, len(ans)- 1
while left <= right:
    mid = (left + right) // 2
    if ans[mid] == q:
        print(mid)
        break
    elif ans[mid] > q:
        left = mid + 1
    else:
        right = mid - 1
    
else:
    print(-1)