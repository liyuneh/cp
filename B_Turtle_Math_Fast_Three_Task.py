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
    a = numbers()

    s = sum(a) % 3
    if s == 0:
        print(0)
        return

    cnt = Counter(x % 3 for x in a)

    if s == 1:
        if cnt[1] >= 1:
            print(1)
        else:
            print(2)
    else:
        print(1)


for _ in range(test_cases()):
    solve()
