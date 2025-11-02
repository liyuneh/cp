import sys
import math
import heapq as heap
import itertools
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
    n , m = numbers()
    arr1 = numbers()
    arr2 = numbers()
    l, r = 0, 0
    ans = []
    
    while l < len(arr1) and r < len(arr2):
        if arr1[l] <= arr2[r]:
            ans.append(arr1[l])
            l += 1
        else:
            ans.append(arr2[r])
            r += 1
    
    if l < n:
        ans = ans + arr1[l:]
    if r < m:
        ans = ans + arr2[r:]
    
    print(*ans)
    return

for _ in range(test_cases(1)):
    solve()
