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
    if len(set(arr)) == 1:
        print(0,(n * (n-1))//2)
        return 
    max_diff = max(arr) - min(arr)
    freq = {}
    for ch in arr:
        freq[ch] = freq.get(ch, 0) + 1
    count = 0
    for key, val in freq.items():
        if key + max_diff in freq:
            count += (freq[key] * freq[key + max_diff])
    
    print(max_diff, count)

    return

for _ in range(test_cases(1)):
    solve()