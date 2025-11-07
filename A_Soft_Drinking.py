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
    arr = numbers()
    a = arr[1] * arr[2] // arr[6]
    b = arr[3] * arr[4]
    c = arr[5] // arr[7]
    k = min(a,b,c) // arr[0]
    print(k)
    return

for _ in range(test_cases(1)):
    solve()