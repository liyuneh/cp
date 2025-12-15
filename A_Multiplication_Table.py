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
    n  , x = numbers()
    t = min(n , x)
    l , r = 1 , t 
    count = 0
    while l <= r:
        if  l * r == x:
            if l == r:
                count += 1
            else:
                count += 2
            l += 1
            r -= 1
        elif l * r > x:
            r -= 1
        else:
            l += 1
    print(count)
    return

for _ in range(test_cases(1)):
    solve()