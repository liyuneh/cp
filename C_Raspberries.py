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
    arr = numbers()
    rem = Counter(c % k for c in arr)

    if k == 2:
        print(0 if rem[0] else 1)
        return

    if k == 3:
        if rem[0]:
            print(0)
        elif rem[2]:
            print(1)
        else:
            print(2)
        return

    if k == 4:
        count_even = rem[2]
        if rem[0]:
            print(0)
        elif count_even >= 2:
            print(0)
        elif count_even == 1 and rem[1]:
            print(1)

        elif rem[3]:
            print(1)
        else:
            print(2)
        return

    if k == 5:
        if rem[0]:
            print(0)
        elif rem[4]:
            print(1)
        elif rem[3]:
            print(2)
        elif rem[2]:
            print(3)
        else:
            print(4)
        return

for _ in range(test_cases()):
    solve()