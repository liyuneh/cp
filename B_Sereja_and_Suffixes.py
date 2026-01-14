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
    n , m = numbers()
    arr = numbers()
    arr = arr[::-1]
    # print(arr)
    seen = set()
    pref = 0
    prefs = []
    for i in range(n):
        if arr[i] not in seen:
            pref += 1
            prefs.append(pref)
            seen.add(arr[i])
        else:
            prefs.append(pref)
    prefs = prefs[::-1]
    # print(prefs)
    for _ in range(m):
        x = number()
        print(prefs[x-1])


    return

for _ in range(test_cases(1)):
    solve()