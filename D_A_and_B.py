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
    arr = word()
    if n <= 2:
        print(0)
    a1 = arr.index('a')
    a2 = len(arr) - arr[::-1].index('a') - 1
    b1 = arr.index('b')
    b2 = len(arr) - arr[::-1].index('b') - 1
    print(a1,a2,b1,b2)
    return

for _ in range(test_cases()):
    solve()