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
    for _ in range(n):
        m = number()
        prod = 1
        count = 0
        res = 2
        for i in range(2,m):
            prod *= i
            count += i
            if prod == count:
                res = max(res, count)
        print(res)
    return

for _ in range(test_cases(1)):
    solve()