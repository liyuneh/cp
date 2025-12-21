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
    n, k = numbers()
    s = word().strip()
    arr = [int(c) for c in s]
    count = 0
    i = 0
    while i < n:
        if arr[i] == 0:
            tramp_idx = -1
            for j in range(max(0, i - k), i):
                if arr[j] == 1:
                    tramp_idx = j
                    break
            if tramp_idx == -1:
                count += 1
            i += 1
        else:
            i += 1
    print(count)
    return

for _ in range(test_cases()):
    solve()
