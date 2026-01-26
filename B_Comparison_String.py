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
    s = word()
    ans = 0
    stack = []
    count = 0
    for c in s:
        if  stack and c == stack[-1]:
            count += 1
        else :
            ans = max(ans, count)
            stack.append(c)
            count = 1
    # print(count)
    ans = max(ans, count)
    print(ans + 1)

    return

for _ in range(test_cases()):
    solve()