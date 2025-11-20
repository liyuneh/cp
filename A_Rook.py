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
    s = word()
    col , row = s[0], s[1]
    cols = "abcdefgh"
    rows = "12345678"
    
    ans = []
    
    for c in cols:
        if c != col:
            ans.append(c + row)
    
    for r in rows:
        if r != row:
            ans.append(col + r)
    print('\n'.join(ans))

    return

for _ in range(test_cases()):
    solve()