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
    a , b = numbers()
    if a % 2 != 0:
        print("NO")
        return
    
    if a % 2 == 0 and b % 2 == 0:
        print("YES")
        return 
    if a % 2 == 0 and b % 2 == 0:
        print("YES")
        return
    if a % 2 == 0 and b % 2 != 0:
        x = a // 2
        if x % 2 == 1:
            print("YES")
        else:
            print("NO")
        return
    
    return

for _ in range(test_cases()):
    solve()