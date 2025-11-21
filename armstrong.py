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

# armstrong number is a number which gives you 
def solve():
    n = number()
    result = 0
    armstrong = n
    count = len(str(n))
    while n > 0:
        result += (n % 10 ) ** count
        n //= 10
    print(result == armstrong)

    return

for _ in range(test_cases()):
    solve()