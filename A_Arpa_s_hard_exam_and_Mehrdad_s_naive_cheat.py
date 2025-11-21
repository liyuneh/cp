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
    if n % 4 == 1 and (n - 1) % 2 == 0:
       print(8)
    elif n % 4 == 2:
        print(4)
    elif n % 4 == 0 and n != 0:
        print(6)
    elif n == 0:
        print(1)
    else:
        print(2)
    return

for _ in range(test_cases(1)):
    solve()