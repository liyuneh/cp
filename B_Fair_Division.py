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
        arr = sorted(numbers())
        total = sum(arr)
        if total % 2 != 0:
            print("NO")
            continue
        count1 , count2 = 0 , 0
        for i in range(len(arr)):
            if arr[i] == 1:
                count1 += 1
            else:
                count2 += 1
        if (count1 == 0 and count2 % 2 == 1) or (count1 % 2 == 1 and count2 % 2 == 0):
            print("NO")
        else:
            print("YES")
    return

for _ in range(test_cases(1)):
    solve()