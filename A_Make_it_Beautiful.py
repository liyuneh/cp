n = int(input())
for _ in range(n):
    k = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    if arr[0] == arr[-1]:
        print("NO")
    else:
        print("YES")
        ans = [arr[-1]]
        for i in range(k-1):
            ans.append(arr[i])  
        print(*ans)      