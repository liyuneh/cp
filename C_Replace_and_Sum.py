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
    n, q = numbers()
    a = numbers()
    b = numbers()
    a.append(0)

    for i in range(n-1, -1, -1):
        a[i] = max(a[i], a[i+1], b[i])

    prefs = [0] * (n+1)

    for i in range(n):
        prefs[i+1] = prefs[i] + a[i]


    ans = []
    for _ in range(q):
        l, r = numbers()
        ans.append(prefs[r] - prefs[l - 1])

    print(*ans)


for _ in range(test_cases()):
    solve()
