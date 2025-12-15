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
    arr = list(str(n)) 
    arr.append('1')
    if arr[0] != '1':
        print("NO")
        return 
    r = 0
    while r < len(arr) - 1:
        if r + 2 < len(arr)  and arr[r:r+3] == ['1', '4', '4']:
            r += 3
        elif r + 1 < len(arr) and arr[r:r+2] == ['1', '4']:
            r += 2
        elif arr[r] == '1':
            r += 1
        else:
            print("NO")
            return
    print("YES")

    return

for _ in range(test_cases(1)):
    solve()