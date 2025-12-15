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
    s , n = numbers()
    ans = []
    for _ in range(n):
        x, y = numbers()
        ans.append([x,y])
    ans.sort(key=lambda x:x[0])
    found = True
    for first , second in ans:
        if s > first:
            s += second
        else:
            found = False
            break
    if found :
        print("YES")
    else:
        print("NO")
    
    
    return

for _ in range(test_cases(1)):
    solve()