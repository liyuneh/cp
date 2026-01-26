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
    if len(set(arr)) == 1:
        print(0)
        return 
    
    if arr[0] == arr[-1]:
        countl = 1
        countr = 1
        for i in range(1, n):
            if arr[i] == arr[i-1]:
                countl += 1
            else:
                break

        for i in range(n-2, -1, -1):
            if arr[i] == arr[i+1]:
                countr += 1
            else:
                break
        print(len(arr) - (countl + countr))
        return 
    if arr[0] != arr[-1]:
        countl = 1
        countr = 1
        for i in range(1, n):
            if arr[i] == arr[i-1]:
                countl += 1
            else:
                break
        for i in range(n - 2, - 1, -1):
            if arr[i] == arr[i+1]:
                countr += 1
            else:
                break
        print(len(arr) - max(countl, countr))
        return 

                
        
    
    return

for _ in range(test_cases()):
    solve()