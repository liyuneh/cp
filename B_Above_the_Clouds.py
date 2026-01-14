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
    s = word()

    right = Counter(s)
    left = Counter()

    ok = False
    for i in range(1, n - 1):
        right[s[i]] -= 1
        left[s[i - 1]] += 1
        if left[s[i]] > 0 or right[s[i]] > 0:
            ok = True
            break

    print("Yes" if ok else "No")


for _ in range(test_cases()):
    solve()
