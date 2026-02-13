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
    per = numbers()
    final = numbers()

    for i in range(n-1,-1,-1):
        if per[i] == final[i]:
            continue
        elif i + 1 < n and final[i] == per[i+1]:
            per[i] = per[i+1]
        elif i - 1 >= 0 and final[i] == per[i-1]:
            per[i] = per[i-1]
        else:
            print("NO")
            return 
    print("YES")
    return

for _ in range(test_cases()):
    solve()