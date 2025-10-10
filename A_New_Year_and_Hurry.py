n , k = map(int,input().split())
s = 240 - k
count = 0
for i in range(1,n + 1):
    if s >= 5 * i:
        s -= (5 * i)
        count += 1
    else:
        continue
print(count)
