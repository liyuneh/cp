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
    if m > n:
        print(-1)
        return 
    if m == n:
        print(n)
        return 
    x = n / 2
    if x % m == 0:
        print(int(x))
        return 
    x = math.floor(x)
    found = False
    for i in range(x + 1, n + 1):
        if i % m == 0:
            found = True
            break
    if found :
        print(i)
    else:
        print(-1)
    return

for _ in range(test_cases(1)):
    solve()