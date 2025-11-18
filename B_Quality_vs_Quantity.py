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
    arr.sort()
    ans1 = arr[0]
    l, r = 1 , n - 1
    ans2 = 0
    ok = False
    while l <= r:
        ans1 += arr[l]
        ans2 += arr[r]
        if ans1 < ans2:
            ok = True
            break
        l += 1
        r -= 1
            
    if ok :
        print("YES")
    else:
        print("NO")
    return

for _ in range(test_cases()):
    solve()