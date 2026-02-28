n , m = map(int, input().split())
ans = []
totala = 0
totalb = 0
for _ in range(n):
    a , b = map(int, input().split())
    totala += a
    totalb += b
    ans.append(abs(a - b))
ans.sort(reverse = True)
# print(ans)
# print(totala)
if totalb > m:
    print(-1)
elif totalb == m:
    print(n)
elif totala <= m:
    print(0)
else:
    count = 0
    found = False
    for i in range(len(ans)):
        totala -= ans[i]
        if totala > m:
            count += 1
        else:
            print(count + 1)
            found = True
            break
    if not found :
        print(-1)       