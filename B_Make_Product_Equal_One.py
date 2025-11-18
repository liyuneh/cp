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
    n = int(input())
    arr = list(map(int, input().split()))
    count_neg = sum(1 for x in arr if x < 0)
    count_zero = sum(1 for x in arr if x == 0)
    ans = 0
    for x in arr:
        if x > 0:
            ans += x - 1
        elif x < 0:
            ans += abs(x) - 1
        else:
            ans += 1
    if count_neg % 2 == 1 and count_zero == 0:
        ans += 2

        
    print(ans)

    return

for _ in range(test_cases(1)):
    solve()