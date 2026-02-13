import sys, math, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint
from heapq import heappush, heappop, heapify
from random import randint
Random = randint(100, 10**4)
Xor = lambda x:x ^ Random

number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yes_no = lambda condition: 'YES' if condition else 'NO'
test_cases = lambda inp=0: number() if not inp else inp

def solve():
    s = word()
    t = word()

    if len(t) == len(s) and s == t:
        print(s)
        return 
    if len(t) == len(s) and s != t:
        print(-1)
        return 
    if s[-1] != t[-1]:
        print(-1)
        return 
    x = math.lcm(len(s), len(t))
    if len(s) < len(t):
        if t * (x // len(t)) == (x // len(s)) * s:
            print((x//len(s)) * s)
        else:
            print(-1)
        return 
    if len(s) > len(t):
        if t * (x // len(t)) == (x // len(s)) * s:
            print((x//len(t)) * t)
        else:
            print(-1)
        return 

    return


for _ in range(test_cases()):
    solve()
