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
    for _ in range(t):
        n = number()
        if n % 3 == 0:
            print(n // 3 , n//3)
        elif (n - 1) % 3 == 0:
            print(math.ceil(n/3), n//3)
        else:
            print(n//3 , math.ceil(n/3)) 
    return

for _ in range(test_cases(1)):
    solve()