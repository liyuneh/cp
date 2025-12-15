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
    if n % 4 == 0 or n % 7 == 0 or n % 47 == 0:
        print("YES")
        return 
    s = str(n)
    found = True
    for c in s:
        if c not in ['4', '7']:
            found = False
            break
    if found:
        print("YES")
    else:
        if n % 4 != 0:
            print("NO")
    return

for _ in range(test_cases(1)):
    solve()