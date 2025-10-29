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
    n , m = numbers()
    arr = sorted(numbers())
    if m < n:
        print(0)
        return 
    l = 0
    res = float('inf')
    for r in range(m):
        if r - l + 1 == n:
            res = min(res, arr[r] - arr[l])
            l += 1
    print(res)
    return

for _ in range(test_cases(1)):
    solve()

    # 5 7 10 10 12 22
