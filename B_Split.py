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
    arr = numbers()
    counter = Counter(arr)
    count = len(set(arr)) if len(set(arr)) != 1 or  len(set(arr)) // 2 != 2 else 0
    for key, values in counter.items():
       if values % 2 ==0:
           count += 1
    print(count)
    return

for _ in range(test_cases()):
    solve()
    # 1 2 3 4 5 4 1 4 1 5 4 6