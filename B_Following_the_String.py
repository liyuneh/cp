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

    ans = [0] * 26 
    s = []
    for i in range(len(arr)):
        for j in range(len(ans)):
            if arr[i] == ans[j]:
                s.append(chr(97+j))
                ans[j] += 1
                break
    print("".join(s))
    return

for _ in range(test_cases()):
    solve()