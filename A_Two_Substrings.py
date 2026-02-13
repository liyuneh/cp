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
    s = word().upper()
    if len(s) < 4 or 'AB' not in s or "BA" not in s:
        print("NO")
    else:
        if ("AB" in s and "BA" in s[s.index("AB") + 2:]) or ("BA" in s and "AB" in s[s.index("BA") + 2:]):
            print("YES")
        else:
            print("NO")
    
    
        
        
    return

for _ in range(test_cases(1)):
    solve()