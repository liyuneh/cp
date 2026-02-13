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
    n , t = numbers()
    if n == 1:
        for i in range(2,10):
            if i % t == 0:
                print(i)
                return 
    if n == 1 and len(str(t)) == 2:
        print(-1)
        return 
    s = ['1'] + (n-1) * ['0']
    start = int("".join(s))
    for i in range(start, start+11):
        if i % t == 0:
            print(i)
            return 
    print(-1)
            
    
    return

for _ in range(test_cases(1)):
    solve()