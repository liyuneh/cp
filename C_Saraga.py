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
    t = word()
    if not any(c  in t for c  in s ) :
        print(-1)
        return 
    k = ""
    for i in range(len(s)):
        if s[i] not in t:
            k += s[i]
        else:
            k += t[ t.index(s[i]):]
            break
    print(k)
    return

for _ in range(test_cases(1)):
    solve()