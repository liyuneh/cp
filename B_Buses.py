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
    n , m ,l, sb , sp = numbers()
    arr = []
    for _ in range(n):
        start, end = numbers()
        arr.append((start,end))
    arr.sort(key=lambda x:x[0])
    for _ in range(m):
        k = number()
        best = (l - k) / sp
        # print(best)

        for a,b in arr:
            if a > k or b <= k:
                continue
            bus = (b - a) / sb
            to_last = (l - b) / sp
            # print(bus)
            # print(to_last)
            # print()


            best = min(best, bus + to_last)
        print(best if best != int(best) else int(best))

    return

for _ in range(test_cases(1)):
    solve()
