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
    n , q = numbers()
    arr = numbers()
    for _ in range(q):
        l , r , k = numbers()
        cur_sum = sum(arr[l-1:r])
        total = sum(arr) - cur_sum + (r - l + 1) * k
        print("YES" if total % 2 == 1 else "NO")

        
    return

for _ in range(test_cases()):
    solve()