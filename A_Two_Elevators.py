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
    a,b,c = numbers()
    t1 = abs(a-1)
    t2 = abs(b-c) + abs(c - 1)
    if t1 < t2:
        print(1)
    elif t1 > t2:
        print(2)
    else:
        print(3) 
    return

for _ in range(test_cases()):
    solve()