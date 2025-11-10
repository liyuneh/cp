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
    arr = word()
    ansa, ansb = [], []
    for i in range(len(arr)):
        if arr[i] == 'a':
            ansa.append(arr[i])
        else:
            ansb.append(arr[i])
    if arr == "".join(ansa) or arr == "".join(ansb):
        print(0)
        return 
    count = 0
    ans3 = ''.join(ansa) + ''.join(ansb)
    if arr == ans3[::-1]:
        print(0)
        return
    for i in range(len(arr)):
        if arr[i] != ans3[i]:
            count += 1
    print(count // 2)
    return

for _ in range(test_cases()):
    solve()