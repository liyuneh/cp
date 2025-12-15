from collections import Counter
s = input()
k = int(input())

l = 0
ans = 0
count = Counter()
for r , char in enumerate(s):
    count[char] += 1

    while count[char] > 1 or r - l + 1 > k:
        count[s[l]] -= 1
        if count[s[l]] == 0:
            del count[s[l]]
        l += 1
    if r - l + 1 == k:
        ans += 1
print(ans)
