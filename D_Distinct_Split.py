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
    n = number()
    s = word()
    if len(set(s)) == n:
        print(n)
        return
    seen = set()
    suffix = [0] * (n + 1)
    for i in range(n-1, -1, -1):
        seen.add(s[i])
        suffix[i] = len(seen)
    seen.clear()
    ans = 0
    for i in range(n):
        if s[i] not in seen:
            seen.add(s[i])
        else:
            l = i
            ans = max(ans, len(seen) + suffix[i])
    print(ans)
    return

for _ in range(test_cases()):
    solve()