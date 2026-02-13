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
    if n % 4 != 0:
        print("NO")
    else:
        even = []
        odd = []
        ans1, ans2  = 2, 1
        for _ in range(n//2):
            even.append(ans1)
            odd.append(ans2)
            ans1 += 2
            ans2 += 2
        odd[-1] = odd[-1] + (n//2)

        final = even + odd
        print("YES")
        print(*final)

    return

for _ in range(test_cases()):
    solve()