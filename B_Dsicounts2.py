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
    n , k = numbers()
    a = numbers()
    b = numbers()
    a.sort()
    add = 0
    prev = 0
    for i in range(k):
        if prev + b[i] - 1 <= n:
            x = a[prev:prev+b[i]- 1]
            add += x
        else:
            continue
    print(add)


    
    return

for _ in range(test_cases()):
    solve()