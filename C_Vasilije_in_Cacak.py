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
    n , k , x = numbers()
    minSum = k * (k + 1) // 2
    maxSum = k * (2*n - k + 1) // 2 
    if minSum <= x <= maxSum:
        print("YES")
    else:
        print("NO")

    return

for _ in range(test_cases()):
    solve()