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
    total = 0
    for i in range(1,n):
        total += abs(arr[i] - arr[i-1])
    last = abs(arr[-2] -arr[-1])
    first = abs(arr[0] - arr[1])
    x = max(last, first)
    gain = 0
    for  i in range(1, n - 1):
        gain = max(gain,abs(arr[i] - arr[i-1]) + abs(arr[i] - arr[i+1]) - abs(arr[i-1] - arr[i+1]))
    print(total - max(x, gain))  
    return

for _ in range(test_cases()):
    solve()