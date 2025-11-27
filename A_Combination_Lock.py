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
    s1 = word()
    s2 = word()
    count = 0
    for i in range(n):
        x = int(s1[i])
        y = int(s2[i])
        k = max(y, x) - min(y , x)
        if k > 5:
            count += (10 - k)
        else:
            count += k
    print(count) 
    return

for _ in range(test_cases(1)):
    solve()