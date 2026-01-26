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

    mx = 0
    for i in range(len(arr)):
        mx += math.ceil(arr[i]/ x)
    mn  = math.ceil(sum(arr) / x)
    print(mn, mx)
    return

for _ in range(test_cases()):
    solve()