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
    n , x = numbers()
    arr = [0] + numbers()
    mx1 = 2 * (x - arr[-1])
    arr.append(0)

    mx = 0 
    for i in range(1, n+1):
        y = arr[i] - arr[i-1]
        if y >= mx:
            mx = y 
    print(max(mx1, mx))
        
        
    return

for _ in range(test_cases()):
    solve()