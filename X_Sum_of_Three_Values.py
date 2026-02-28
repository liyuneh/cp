import sys, math, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint
from heapq import heappush, heappop, heapify
from random import randint
Random = randint(100, 10**4)
Xor = lambda x:x ^ Random

number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yes_no = lambda condition: 'YES' if condition else 'NO'
test_cases = lambda inp=0: number() if not inp else inp

def solve():
    n , x = numbers()
    arr = numbers()
    arr.sort()

    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i+1]:
            continue
        l , r = i + 1, n - 1
        while l < r:
            z = arr[i] + arr[l] + arr[r]
            if z == x:
                print(arr[i], arr[l], arr[r])
                return 
            
    print(-1)
    return


for _ in range(test_cases(1)):
    solve()
