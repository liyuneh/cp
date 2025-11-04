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
    p = word()
    s = word()
    l, r = 0, 0
    while l < len(p) and r < len(s):
        if p[l] == s[r]:
            while r < len(s) - 1 and s[r] == s[r + 1]:
                r += 1
            l += 1
            r += 1
        else:
            break
    print("YES" if l == len(p) and r == len(s) else "NO")

for _ in range(test_cases()):
    solve()
