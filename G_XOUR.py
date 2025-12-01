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
    arr1 = arr.copy()
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] ^ arr[j] < 4 and arr[i] > arr[j]:
                arr[i] , arr[j] = arr[j], arr[i]
                break
        if arr == arr1:
            break
        arr1 = arr.copy()
    print(*arr)

    return

for _ in range(test_cases()):
    solve()