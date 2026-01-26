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

    if 0 in set(arr) and len(set(arr)) == 1:
        print(0)
        return 
    if 0 not in set(arr):
        print(1)
        return
    start = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            start = i
            break
    found = False
    for i in range(start, len(arr) - 1):
        if arr[i] == 0 and arr[i+1] != 0:
            found = True
            break
    if found:
        print(2)
    else:
        print(1)

    return

for _ in range(test_cases()):
    solve()