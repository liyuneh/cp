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
    arr = a[::-1]
    total = sum(a)
    i = n
    x = 0
    while i > 1:
        first = arr.pop()
        second = arr.pop()
        if first >= 0 and second >= 0:
            x += first
            arr.append(second)
        elif first < 0 and  second < 0:
            x -= second
            arr.append(first)
        else:
            if first > 0 and second < 0:
                if abs(first) > abs(second):
                    x += first
                    arr.append(second)
                else:
                    x -= second
                    arr.append(first)
            elif first < 0 and second > 0 :
                if abs()
    return
for _ in range(test_cases()):
    solve()
