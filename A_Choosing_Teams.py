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
    n , k = numbers()
    arr = sorted(numbers())
    l  = 0
    count = 0
    for r in range(len(arr)):
        if arr[r] + k <= 5:
            if r - l + 1 == 3:
                count += 1
                l = r + 1
        else:
            break
    print(count)
    return

for _ in range(test_cases(1)):
    solve()

    # 0 0 0 1 1 1  2 2 3 3 4 4