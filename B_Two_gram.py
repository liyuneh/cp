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
    s = word()
    l = 0 
    freq = {}
    for r in range(len(s)- 1):
        gram = s[r:r+ 2]
        freq[gram] = freq.get(gram, 0) + 1
    freq1 = sorted(freq.items(), key = lambda x:(-x[1], x[0]))
    res = freq1[0][0]
    print(res)
    
    return

for _ in range(test_cases(1)):
    solve()