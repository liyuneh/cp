t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    x = len(set(s))
    seen = set()
    prev = 0
    if len(set(s)) == len(s):
        print(len(s))
        continue
    suffix = []
    same = set()
    for i in range(len(s) - 1, -1, -1):
        if s[i] not in seen:
            same.add(s[i])
        suffix.append(len(same))
    suffix.reverse()
    for i in range(len(s)):
        if s[i] not in seen:
            seen.add(s[i])
        else:
            prev = max(prev, len(seen) + suffix[i] )
    print(prev)