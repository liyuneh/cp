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
    a , b = numbers()
    if a == b:
        print(0)
    elif a > b:
        if a % 2 == b % 2:
            print(1)
        else:
            print(2)
    else:
        if a % 2 != b % 2:
            print(1)
        else:
            print(2)
    return

for _ in range(test_cases()):
    solve()