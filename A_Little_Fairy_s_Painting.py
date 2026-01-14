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
    seen = set(arr)
    k = len(seen)
    if k == 1:
        print(arr[0])
        return 
    cur = k
    while True:
        if cur in seen:
            print(cur)
            return 
        else:
            seen.add(cur)
        cur += 1
    
    
    


    return

for _ in range(test_cases()):
    solve()