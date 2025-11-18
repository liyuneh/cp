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
    arr =  numbers()
    res = []
    for i  in range(len(arr) - 2):
        l , r = i + 1, n - 1
        while l < r:
            if arr[i] + arr[l] <= arr[r]:
                res.append(i+ 1)
                res.append(l + 1)
                res.append(r + 1)
                break
            else:
                r -= 1
        if res:
            break

    if res :
        print(*res)
    else:
        print(-1)
    return

for _ in range(test_cases()):
    solve()