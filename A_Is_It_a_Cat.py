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
    s = word().lower()
    start = "meow"
    if any(c not in start for c in s):
        print("NO")
        return
    ans = [s[0]]
    for i in range(1, n):
        if s[i] != s[i - 1]:
            ans.append(s[i])
    print("YES" if ''.join(ans) == start else "NO")

for _ in range(test_cases()):
    solve()
