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
    arr = numbers()
    four = arr.count(4)
    two = arr.count(2)
    ones = arr.count(1)
    threes = arr.count(3)
    total = four

    pairs = min(ones, threes)
    total += threes 
    ones -= pairs

    total += (two // 2)
    two = two % 2
    
    if two == 1:
        total += 1
        ones = max(0 , ones - 2)
    
    total += (ones + 3) // 4
    print(total )

    return

for _ in range(test_cases(1)):
    solve()