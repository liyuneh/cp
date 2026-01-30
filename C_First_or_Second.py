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
    a = numbers()
    q = deque(a)
    mx = 0
    while len(q) > 1:
        x1 = q.popleft()
        x2 = q.popleft()
        if x1 > 0 and x2 > 0:
            mx += (x1)
            q.appendleft(x2)
        elif x1 > 0 and x2 < 0:
            mx -= (x2)
            q.appendleft(x1)
        elif x1 < 0 and x2 < 0:
            mx -= (x2)
            q.appendleft(x1)
        elif x1 < 0 and x2 > 0:
            mx += x1
            q.appendleft()


    return
for _ in range(test_cases()):
    solve()
