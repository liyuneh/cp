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
    if n == 1 :
        print(k)
        return
    if n == k or k == 1 or n % k == 0:
        print(1)
        return
    if n != k and k != 1:
        print(math.ceil(max(n, k) / min(n , k)))
        return
    return

for _ in range(test_cases()):
    solve()