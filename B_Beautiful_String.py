import sys
import math
import heapq as heap
import itertools
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
    ans = []
    for i in range(n):
        if s[i] == '0':
            ans.append(i + 1)
    print(len(ans))
    print(*ans)
    return

for _ in range(test_cases()):
    solve()
