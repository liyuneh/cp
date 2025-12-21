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
    arr = numbers()
    if k == 4:
        counter = Counter(arr)
        seen = set(arr)
        if 2 in seen:
            if counter[2] >= 2:
                print(0)
                return 
    divisible = False
    for c in arr:
        if c % k == 0:
            divisible = True
            break
    if divisible :
        print(0)
    else:
        max_m = arr[0] % k
        for c in arr:
            if c % k > max_m :
                max_m = c % k
        print(k - max_m) 
    
    return

for _ in range(test_cases()):
    solve()