from collections import defaultdict
n  = int(input())

for _ in range(n):
    t = int(input())
    s = list(map(int, input().split()))
    table = defaultdict(int)
    for num in s:
        table[num] += 1
    for idx, num in enumerate(s):
        if table[num] == 1:
            print(idx + 1)
            break