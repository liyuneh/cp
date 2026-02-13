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
    n = word()
    x = str(n)
    if x[:len(x) // 2 + 1] != x[len(x) // 2 + 1:] and len(x) % 2 != 0:
        print(0)
        return 
    if len(x) == 2 and x[0] != x[1]:
        print(0)
        return 
    if len(x) == 2 and x[0] == x[1]:
        print(x[0])
        return 
    y = list(x)
    ans = []
    if len(y) % 3 == 0 and len(y) % 2 == 0:
        a = "".join(y[:len(y)//2])
        b = "0".join(y[:len(y)// 2])
        for i in range(len())


    
    
    return

for _ in range(test_cases()):
    solve()