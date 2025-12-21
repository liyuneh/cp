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
    b = numbers()
    k = 0
    if n == 1:
        print(max(k -a[0], b[0] - k))
        return 
    if n == 2:
        print(max((0-min(a[0], b[0]) if a[0] * b[0] < 0 or (a[0] < 0 and b[0] < 0  ) else max(a[0], b[0])) - a[1], b[1] - min(a[0], b[0])) )
        return 
    if n >= 3:
        

    return

for _ in range(test_cases()):
    solve()