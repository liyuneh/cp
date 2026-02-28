n = int(input())
ans = []
for _ in range(n):
    a, b = map(int, input().split())
    ans.append([a,b])
mn = max(ans[0])
count = 1
flag = True
for i in range(1,len(ans)):
    if ans[i][0] <= mn and ans[i][1] <= mn:
        mn = max(ans[i][0], ans[i][1])
        count += 1
    elif ans[i][0] <= mn or ans[i][1] <= mn:
        mn = min(ans[i][0], ans[i][1])
        count += 1
    else:
        flag = False
        break
if count == len(ans) and flag:
    print("YES")
elif count < len(ans) or  not flag:
    print("NO")