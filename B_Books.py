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
    n , t = numbers()
    arr = numbers()
    Sum = 0
    l = 0
    count = 0
    for i in range(len(arr)):
        while l < n and Sum + arr[l] <= t:
            Sum += arr[l]
            l += 1
        count = max(count , l - i)
        Sum -= arr[i]
    
    print(count)

    return

for _ in range(test_cases(1)):
    solve()