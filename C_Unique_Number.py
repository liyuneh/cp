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
    total = sum([i for i in range(1,10)])
    if total < n:
        print(-1)
    else:
        res = []
        i = 9
        while n > 0:
            x = min(n , i)
            if x == n:
                res.append(x)
                break
            else:
                n -= i
                res.append(x)
                i -= 1
        res.reverse()
        print(''.join(map(str, res)))

    return

for _ in range(test_cases()):
    solve()