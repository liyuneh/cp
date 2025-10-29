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
    t = number()
    ans = []
    for _ in range(t):
        x = []
        y = []
        for i in range(4):
            a,b = numbers()
            x.append(a)
            y.append(b)
        area = (max(x) - min(x)) * (max(y) - min(y))
        print(area)

        
    return

for _ in range(test_cases(1)):
    solve()