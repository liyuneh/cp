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
    def factorial(n):
        return math.factorial(n)
    
    ans = [1]
    n , d = numbers()
    x = factorial(n) * d
    if x % 3 == 0:
        ans.append(3)
    if d == 5:
        ans.append(5)
    if n >= 3 or d == 7:
        ans.append(7)
    if x % 9 == 0:
        ans.append(9)
    print(*ans)
    return

for _ in range(test_cases()):
    solve()