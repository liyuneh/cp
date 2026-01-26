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
    n , k , q = numbers()
    arr = numbers()
    ans = 0
    count = 0
    for r in range(n):
        if arr[r] > q:
            if count >= k:
                x = count - k + 1
                ans += (x*(x+1))//2
            count = 0
        else:
            count += 1
    if count >= k:
        x = count - k + 1
        ans += (x*(x+1)) // 2


    print(ans)
    return

for _ in range(test_cases()):
    solve()