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
    n1 = number()
    s1 = word()
    n2 = number()
    s2 = word()
    direction = word()
    q = deque(s1)
    for i in range(len(direction)):
        if direction[i] == 'V':
            q.appendleft(s2[i])
        else:
            q.append(s2[i])
    print("".join(q))
    return

for _ in range(test_cases()):
    solve()