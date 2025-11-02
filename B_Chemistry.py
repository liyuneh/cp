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
    n , k = numbers()
    s = word()
    counter = Counter(s)
    count = 0
    for key,  val in counter.items():
        if val % 2 == 1:
            count += 1
    if count > k + 1 :
        print("NO")
    else:
        a = k - count
        print("YES")
    return

for _ in range(test_cases()):
    solve()