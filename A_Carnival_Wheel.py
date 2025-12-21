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
    l , a, b = numbers()
    seen = set()
    count = 0
    max_m  = 0
    for i in range(l ):
        count += 1
        x = (a + count * b) % l
        if x not in seen:
            if max_m < x:
                max_m = x
            seen.add(x)
    print(max_m)
        
        
        
    return

for _ in range(test_cases()):
    solve()