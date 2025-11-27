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
    n , m = numbers()
    arr = numbers()
    countless = 0
    countmore = 0
    for i in range(len(arr)):
        if m > arr[i]:
            countless += 1
        elif m < arr[i]:
            countmore += 1
    if countmore >= countless:
        print(m + 1)
    else:
        print(m - 1)
    return

for _ in range(test_cases()):
    solve()