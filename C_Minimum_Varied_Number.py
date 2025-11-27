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
    if n < 10:
        print(n)
        return 
    i = 9
    ans = []
    while n > 0:
        k = min(i , n)
        ans.append(k)
        n -= k
        i -= 1
    ans.reverse()
    print(''.join(map(str, ans)))
    
    return

for _ in range(test_cases()):
    solve()