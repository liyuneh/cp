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
    even , odd = [] , []
    if len(arr) <= 2:
        print(*arr)
        return
    if len(arr) % 2 == 1:
        odd = arr[:len(arr)// 2 + 1]
        even = arr[len(arr) // 2 + 1:]
    else:
        odd = arr[:len(arr) // 2]
        even = arr[len(arr)//2 :]
    even.reverse()
    ans = []
    l , r = 0, 0

    while l < len(odd) and r < len(even):
        ans.append(odd[l])
        ans.append(even[r])
        l += 1
        r += 1
    if l < len(odd):
        ans = ans + odd[l:]
        print(*ans)
        return 
    if r < len(even):
        ans = ans + even[r:]
        print(*ans)
        return
    print(*ans)
    
    return

for _ in range(test_cases()):
    solve()