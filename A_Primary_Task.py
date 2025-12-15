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
    s1 = s[:2]
    s2 = s[2:]
    if s2[0] == '0':
        print("NO")
    elif s1 != '10':
        print("NO") 
    elif s2[0] != '0'  and int(s2) < 2:
        print("NO")
    else:
        print("YES")

    return

for _ in range(test_cases()):
    solve()