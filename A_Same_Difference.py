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
    s = word()
    count = 0
    if len(set(s)) <= 1:
        print(0)
    else:
        s = s[::-1]
        l = 0
        for i in range(1,len(s)):
            if s[i] != s[l]:
                count += 1
            else:
                continue
        print(count)
    return

for _ in range(test_cases()):
    solve()