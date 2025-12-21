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

from itertools import permutations
def solve():
    n , j , k = numbers()
    perm = permutations(str(n))
    ans = [''.join(p)  for p in perm]

    x = ans[j-1]
    y = ans[k-1]
    count_a = 0
    count_b = 0
    for i in range(len(x)):
        if x[i] == y[i]:
            count_a += 1
    seen = set(y)
    for i in range(len(x)):
        if x[i] != y[i] and x[i] in seen:
            count_b += 1
    print(f"{count_a}A{count_b}B")

    return

for _ in range(test_cases()):
    solve()