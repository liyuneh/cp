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
    q = deque()
    for i in range(len(arr)):
        q.append((i+1, arr[i]))
    while len(q) != 1:
        if q[0][1] <= m:
            q.popleft()
        else:
            idx, val = q.popleft()
            val -= m
            q.append((idx, val))
    print(q[0][0])
    

    return

for _ in range(test_cases(1)):
    solve()
