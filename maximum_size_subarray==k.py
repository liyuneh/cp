arr = list(map(int, input().split(',')))
k = int(input())

seen = {0:-1}

pref = 0
res = 0

for i  ,ch in enumerate(arr):
    pref += ch
    if pref - k in seen:
        res = max(res, i - seen[pref - k] )
    if pref - k not in seen:
        seen[pref] = i
print(res)
