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
    arr = [i for i in range(1, n+1)]
    if n <= 2:
        print(*arr)
        return
    little = arr[:n//2]
    # print(little)

    bigg = arr[n//2:][::-1]
    # print(bigg)
    ans = []
    mn = min(len(bigg), len(little))
    i = 0
    while i < mn:
        ans.append(bigg[i])
        ans.append(little[i])
        i += 1
    if i < len(little):
        ans.append(little[-1])
    elif i < len(bigg):
        ans.append(bigg[-1])
    ans.reverse()
    print(*ans)
    return

for _ in range(test_cases()):
    solve()
