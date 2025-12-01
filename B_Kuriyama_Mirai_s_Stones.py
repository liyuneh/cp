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
    pref1 = [0] * (n + 1)
    for i in range(1,n+1):
        pref1[i] = pref1[i-1] + arr[i-1]
    ans = sorted(arr)
    pref2 = [0] * (n + 1)
    for i in range(1, n + 1):
        pref2[i] =pref2[i-1] + ans[i-1]
    
    m = number()

    for _ in range(m):
        type, l , r = numbers()
        if type == 1:
            print(pref1[r] - pref1[l-1])
        else:
            print(pref2[r] - pref2[l-1])

    return

for _ in range(test_cases(1)):
    solve()