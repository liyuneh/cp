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
    if (n % 3 == 0 and n % 2 == 0) or (n % 3 == 0 and n % 2 != 0):
        print(abs(n // 3))
        return
    if abs(n) == 2:
        print(1)
        return
    if n == 1:
        print(2)
        return
    n = abs(n)
    if n % 3 == 2:
        print(1 + (n - 2) // 3)
        return 
    if  n % 3 == 1:
        if n % 2 == 0:
            x = n // 2
            print(min(x, n // 3 + 1))
            return
        else:
            print((n - 4) // 3 + 2)
            return 
    return

for _ in range(test_cases()):
    solve()