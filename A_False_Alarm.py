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
    n , x = numbers()
    arr = numbers()
    left = arr.index(1)
    right = n - 1-arr[::-1].index(1)
    if (right - left + 1) > x:
        print("NO")
    else:
        print("YES")

    return

for _ in range(test_cases()):
    solve()