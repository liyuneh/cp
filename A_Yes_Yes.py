import sys, math, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint
from heapq import heappush, heappop, heapify


number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yes_no = lambda condition: 'YES' if condition else 'NO'
test_cases = lambda inp=0: number() if not inp else inp


def solve():
    s = word()
    l = math.ceil(len(s) / 3 + 3)
    k = "Yes" * l
    if any(c not in k for c in s):
        print("NO")
        return 
    c = k.index(s[0])
    l = 0
    for i in range(c, len(k)):
        if l < len(s) and s[l] == k[i]:
            l += 1
        else:
            break
    if l == len(s):
        print("YES")
    else:
        print("NO")
    return

for _ in range(test_cases()):
    solve()