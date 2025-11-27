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
    a, b = numbers()
    if a % 2 == 0 and b % 2 == 1:
        print(-1)
    elif a % 2 == 1 and b % 2 == 0:
        k = b // 2
        if (a * k + b // k ) % 2 == 0:
            print(a * k + b//k)
        else:
            print(-1)
    elif a % 2 == 1 and b % 2 == 1:
        print( a * b  + b // b)
    else:
        k = b // 2
        print(a * k + b//k)

    return

for _ in range(test_cases()):
    solve()