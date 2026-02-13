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
    if k > n :
        print(-1)
        return 
    if k == n:
        print(0)
        return

    count2 = 0
    while n > k:
        count2 += 1
        x , y = n - (n//2), n // 2
        if x  == k or y == k:
            print(count2)
            return
            
        n = x if x % 2 == 1 else y
    
    
    print(-1)
    return

for _ in range(test_cases()):
    solve()