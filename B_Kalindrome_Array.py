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
    if arr == arr[::-1] or len(arr) <= 2:
        print("YES")
        return
    l , r = 0 , n - 1
    while l < r and arr[l] == arr[r]:
        l += 1
        r -= 1
    if l >= r:
        print("YES")
        return 
    x = arr[l]
    y = arr[r]
    arr_x = [v for v in arr if v != x]
    arr_y = [v for v in arr if v != y]
    if arr_x == arr_x[::-1] or arr_y == arr_y[::-1]:
        print("YES")
    else:
        print("NO")
    return

for _ in range(test_cases()):
    solve()