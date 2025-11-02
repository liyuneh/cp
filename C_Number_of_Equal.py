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
    n , m = numbers()
    arr1 = numbers()
    arr2 = numbers()
    count = 0
    counter1  = Counter(arr1)
    counter2 = Counter(arr2)
    for keys , values in counter1.items():
        if keys in counter2:
            count += (values * counter2[keys])
    print(count)
    
    return

for _ in range(test_cases(1)):
    solve()