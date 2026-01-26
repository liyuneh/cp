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
    x, y = numbers()
    a, b = numbers()
    if x == y and x == 0:
        print(0)
        return 
    if x == y and x != 0:
        print(min(x*b, (x+y) * a))
        return 
    z = max(x, y)
    c = min(x, y)
    print(min(a*(x+y), a*(z-c) + b* c))


    return

for _ in range(test_cases()):
    solve()