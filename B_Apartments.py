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
    n , m , k = numbers()
    arr = numbers()
    arr2 = numbers()

    arr.sort()
    arr2.sort()
    count = 0

    i , j = 0 ,0
    while i < n and j < m:
        if arr2[j] < arr[i] - k:
            j += 1
        elif arr2[j] > arr[i] + k:
            i += 1
        else:
            count += 1
            i += 1
            j += 1
    print(count)


    return


for _ in range(test_cases(1)):
    solve()
