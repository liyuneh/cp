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
    a1,a2,a3,a4 = numbers()
    s = word()
    count = 0
    for c in s:
        if c == '1':
            count += a1
        elif c == '2':
            count += a2
        elif c == '3':
            count += a3
        else:
            count += a4
    print(count)
    return

for _ in range(test_cases(1)):
    solve()