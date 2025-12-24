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
    n  ,k = numbers()
    arr = sorted(numbers())
    if k == 0:
        print(arr[0] - 1 if arr[0] - 1 >= 1 else -1)
        return 
    freq = {}
    for ch in arr:
        freq[ch] = freq.get(ch, 0) + 1
    ans = [val for val in freq.values()]
    pref = 0
    prefs = [1] * len(ans)
    for i in range(len(ans)):
        pref += ans[i]
        prefs[i] = pref
    seen = set(prefs)
    
    if k in seen:
        print(arr[k-1])
        return 
    else:
        print(-1)
    return

for _ in range(test_cases(1)):
    solve()