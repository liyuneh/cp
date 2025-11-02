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
    t = number()
    for _ in range(t):
        s = word()
        countone = s.count("1")
        countzero = s.count("0")
        moves = min(countone, countzero)
        if  moves % 2 == 1:
            print("DA")
        else:
            print("NET")
    return

for _ in range(test_cases(1)):
    solve()