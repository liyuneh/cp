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
    a = numbers()
    voucher = numbers()
    a.sort(reverse = True)
    voucher.sort()
    total = sum(a)

    prev = -1
    add = 0
    for v in voucher:
        if v + prev < n:
            add += a[v + prev ]
            prev = v + prev 
        else:
            break
    print(total - add)
    
    
    return

for _ in range(test_cases()):
    solve()