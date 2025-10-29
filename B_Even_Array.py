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
    arr = numbers()
    countodd , counteven = 0, 0
    for i in range(len(arr)):
        if i % 2 == 0 and arr[i] % 2 == 1:
            counteven += 1
        elif i % 2 == 1 and arr[i] % 2 == 0:
            countodd += 1
    if countodd == counteven:
        print(countodd)
    else:
        print(-1)
    
    return

for _ in range(test_cases()):
    solve()