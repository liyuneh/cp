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
    count = 0
    while n != 1:
        if n % 6 == 0:
            n //= 6
        elif n % 3 == 0:
            n *= 2
        else:
            print(-1)
            return 
        count += 1
    print(count)
        
    return

for _ in range(test_cases()):
    solve()
        