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
    t = number()
    for _ in range(t):
        n = number()
        arr = numbers()
        g = 0
        for x in arr:
            g = math.gcd(g, x)
        if g == 1:
            print(2)
        else:
            for i in range(2, 100):
                if math.gcd(i, g) == 1:
                    print(i)
                    break

for _ in range(test_cases(1)):
    solve()
