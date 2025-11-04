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
    k = number()
    arr = numbers()
    arr.sort()
    Sum = 0
    count = 0
    if sum(arr) < k:
        print(-1)
        return 
    for r in range(12):
        if Sum < k:
            x = arr.pop()
            Sum += x
            count += 1
        else:
            break
    print(count)

    return

for _ in range(test_cases(1)):
    solve()