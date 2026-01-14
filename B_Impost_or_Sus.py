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
    s = word()
    arr = list(s)
    count = 0
    if arr[0] == 'u':
        count += 1
    if arr[-1] =='u':
        count += 1
    if arr[0] == 'u':
        arr[0] = 's'
    if arr[-1] == 'u':
        arr[-1] = 's'
    ans = 0
    for i in range( len(arr)):
        if arr[i] == 's':
            count += ans//2
            ans = 0
        else:
            ans += 1

    print(count)
    return

for _ in range(test_cases()):
    solve()