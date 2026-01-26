n = int(input())
ans = sorted(list(map(int, input().split())))
count = 0
for i in range(len(ans)):
    s = ans[-1] - ans[i]
    count += s
print(count)