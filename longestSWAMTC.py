# from collections import dict
s = input()

l = 0
count = {}
res = 0
for r in range(len(s)):
    count[s[r]] = count.get(s[r], 0) + 1

    while len(count) > 2:
        count[s[l]] -= 1
        if count[s[l]] == 0:
            del count[s[l]]
        l += 1
    res = max(res, r - l + 1)
print(res)