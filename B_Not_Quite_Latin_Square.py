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
    t = number()
    for _ in range(t):
        s = ""
        for i in range(3):
            arr = word()
            for j in range(3):
                if arr[j].isalnum():
                    s += arr[j]
        counter = Counter(s)
        for key, value in counter.items():
            if value == 2:
                print(key)
                break
    return

for _ in range(test_cases(1)):
    solve()
