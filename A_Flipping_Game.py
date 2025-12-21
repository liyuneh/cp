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
    original_ones = arr.count(1)
    ans = arr[:]
    for c in range(n):
        if arr[c] == 1:
            arr[c] = -1
        else:
            arr[c] = 1
    add = arr[0]
    max_m = arr[0]
    for c in range(1, len(arr)):
        add = max(arr[c], add+arr[c])
        max_m = max(max_m , add)
    if max_m < 0:
        print(original_ones - 1)
    elif max_m == len(arr):
        print(max_m)
    else:
        print(original_ones + max_m)

    return

for _ in range(test_cases(1)):
    solve()