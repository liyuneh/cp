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
    m, f , n = numbers()
    arr = numbers() 

    # Sum = 0
    # prev = f
    # i = 0
    # first = 0
    # while i  < n :
    #     if prev + arr[i] <= m :
    #         prev +=  arr[i]
    #     else:
    #         if first == 0:
    #             Sum += min(prev-1, m-1)
    #             first = 1
    #         else:
    #             Sum += min(prev, m-1)
    #         prev = arr[i]
    #     i += 1
    # Sum += min(prev, m) 
    # print(Sum)

    ans = f
    for i in range(len(arr)):
        ans += min(arr[i], m - 1)
    print(ans)
    
    return

for _ in range(test_cases()):
    solve()