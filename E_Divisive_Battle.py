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
    n = number()
    arr = numbers()
    if sorted(arr) == arr:
        print("Bob")
        return 
    flag = True
    for i in range(len(arr)):
        if i % 2 == 0 and arr[i] % 2 != 0:
            print("Bob")
            flag = False
            return 
        elif i % 2 == 1 and arr[i] % 2 != 0:
            print("Alice")
            flag = False
            return 
        elif i % 2 == 0 and arr[i] % 2 == 0:
            arr[i] = (arr[i] // (arr[i] // 2))
        elif i % 2 == 1 and arr[i] % 2 == 0:
            arr[i] = (arr[i] // (arr[i] // 2))
    if flag :
        if sorted(arr) == arr:
            print("Bob")
        else:
            print("Alice")
    return


for _ in range(test_cases()):
    solve()
