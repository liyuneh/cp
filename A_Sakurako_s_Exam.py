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
    total = a * 1 + b * 2
    if total % 2 == 1:
        print("NO")
        return
    if a % 2 == 1:
        print("NO")
    else:
        if b % 2 == 0:
            print("YES")
        else:
            x = a - 2
            if x >= 0 and  x % 2 == 0:
                print("YES")
            else:
                print("NO")


    
    return

for _ in range(test_cases()):
    solve()