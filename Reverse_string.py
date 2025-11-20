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
    n = word()
    k = number()
    l = 0
    s = ""
    count = 0
    while l< len(n):
        r = l + k
        segment = n[l:r]
        if len(segment) < k:
            s += segment
            break
        if count % 2 == 0:
            s += segment[::-1]
        else:
            s += segment
        count += 1
        l += k
    print(s)
    

    return

for _ in range(test_cases(1)):
    solve()