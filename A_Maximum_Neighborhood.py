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
    res = 0
    for i in range(1,n ** 2 + 1):
        total = i
        total += i - n if i - n > 0 else 0
        total += i + 1 if i + 1 <= n ** 2 and i % n != 0 else 0
        total += i + n if i + n <= (n ** 2) else 0
        total += i - 1 if i - 1 > 0 and (i - 1) % n != 0 else 0
        res = max(res, total)

    print(res)

        

    
    return

for _ in range(test_cases()):
    solve()