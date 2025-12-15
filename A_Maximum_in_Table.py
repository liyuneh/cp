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
    ans = [[1] * n for _ in range(n)]
    for i in range(1, n):
        for j in range(1,n):
            ans[i][j] = ans[i-1][j] + ans[i][j-1]
    print(ans[n-1][n-1])

    return

for _ in range(test_cases(1)):
    solve()