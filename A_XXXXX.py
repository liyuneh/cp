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
        n , k = numbers()
        arr = numbers()
        count = ans = 0
        l = 0
        total = sum(arr)
        if total % k != 0:
            print(n)
            continue
        while l <  n and arr[l] % k == 0:
            l += 1
        r = n - 1
        while r >= 0 and arr[r] % k == 0:
            r -= 1
        count = max(n - l  - 1, r)
        print(count if count > 0 else -1)
    return

for _ in range(test_cases(1)):
    solve()