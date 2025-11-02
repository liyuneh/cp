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
    nums = numbers()
    count = 5
    while count > 0:
        x = min(nums)
        nums.remove(x)
        nums.append(x + 1)
        count -= 1
    
    print(math.prod(nums))
    return

for _ in range(test_cases()):
    solve()

    # 1 10 10 
    # 2 3 4
    # 5 6 8