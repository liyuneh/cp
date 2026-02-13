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
    n , k = numbers()
    arr = numbers()
    # arr.sort()

    if all(arr[i] % k == 0 for i in range(len(arr))):
        print(0)
        return 
    freq = defaultdict(int)
    for ch in arr:
        if ch % k != 0:
            freq[k - (ch % k)] += 1
    # print(freq)
    mx = 0
    for key , val in freq.items():
        if key != 0:
            mx = max(mx, key + (val-1) * k)
    print(mx + 1)
    return

for _ in range(test_cases()):
    solve()