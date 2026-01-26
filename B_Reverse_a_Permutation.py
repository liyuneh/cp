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

    nums = sorted(arr, reverse = True)
    
    l , r = -1, -1
    for i in range(len(arr)):
        if nums[i] != arr[i]:
            l = i
            break
    if l == -1:
        print(*arr)
        return 
    k = -1
    for i in range(len(arr)-1, 0,-1):
        if nums[i] != arr[r]:
            k = i
            break
    segment = arr[l:k+1]
    mx = max(segment)
    for i in range(len(arr) - 1, 0 , - 1):
        if arr[i] == mx:
            r = i
            break
    new = arr[:l] + arr[l:r+1][::-1] + arr[r+1:]
    print(*new)
    


for _ in range(test_cases()):
    solve()
