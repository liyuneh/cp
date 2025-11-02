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
    m = list(word())
    count = 0
    for r in range(n):
        if m[r] == '1':
            m[r] = '0'
            count += m.count('1')
            m[r] = '1'
        else:
            m[r] = '1'
            count += m.count('1')
            m[r] = '0'
    print(count)
    return

for _ in range(test_cases()):
    solve()