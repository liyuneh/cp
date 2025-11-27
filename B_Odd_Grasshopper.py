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
    x , d = numbers()
    if x % 2 == 0:
        if d % 4 == 0:
            print(x)
        elif d % 4 == 1:
            print(x - d )
        elif d % 4 == 2:
            print(x + 1)
        else:
            print(x + d + 1)
    else:
        if d % 4 == 0 :
            print(x)
        elif d % 4 == 1:
            print(x + d)
        elif d % 4 == 2:
            print(x -  1)
        else:
            print(x - d - 1)

    return

for _ in range(test_cases()):
    solve()

   