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
    if n <= 1:
        print("YES")
        return 
    total = sum(arr)
    avg = total // n
    count = 0
    found = True
    for i in range(n):
        count += arr[i]
        if count / (i + 1) < avg:
            found = False
            break
    if found:
        print("YES")
    else:
        print("NO")
    
    return

for _ in range(test_cases()):
    solve()