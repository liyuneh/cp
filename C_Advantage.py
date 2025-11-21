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
    max1 = max(arr)
    max2 = -1
    count_max1 = 0

    for x in arr:
        if x == max1:
            count_max1 += 1
        elif x > max2:
            max2 = x

    result = []
    for x in arr:
        if x == max1:
            if count_max1 > 1:
                result.append(0)
            else:
                result.append(x - max2)
        else:
            result.append(x - max1)

    print(*result)

for _ in range(test_cases()):
    solve()
