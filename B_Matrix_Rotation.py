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
    a = numbers()
    b = numbers()

    for _ in range(4):
        if a[0] < a[1] and b[0] < b[1] and a[0] < b[0] and a[1] < b[1]:
            print("YES")
            return
        a[0], a[1], b[1], b[0] = b[0], a[0], a[1], b[1]

    print("NO")


for _ in range(test_cases()):
    solve()
