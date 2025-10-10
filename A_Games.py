n = int(input())
ans = []
for i in range(n):
    k = list(map(int, input().split()))
    ans.append(k)
count = 0
for i in range(n):
    for j in range(len(ans)):
        if i != j:
            if ans[i][0] == ans[j][1]:
                count += 1
print(count)