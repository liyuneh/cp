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
    a, b = sorted(numbers(), reverse=True)
    # print(a, b)

    first , next = 0 ,0 
    count = 0
    itr = 1
    while True:
        first, next = next + itr, first
        if first <= a and next <= b:
            count += 1
            itr *= 2
        else:
            break
    print(count)
        

    

    return

for _ in range(test_cases()):
    solve()


    # 1 4 16 32 128 