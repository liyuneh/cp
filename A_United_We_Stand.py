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
    a = numbers()
    
    if len(set(a)) == 1:
        print(-1)
        return
    
    max_val = max(a)
    b = [x for x in a if x == max_val]
    c = [x for x in a if x != max_val]
    
    print(len(b), len(c))
    print(*b)
    print(*c)

for _ in range(test_cases()):
    solve()
# Passionate problem solver skilled in data structures, algorithms, and clean coding. Solved diverse LeetCode challenges with focus on efficiency, logic, and optimization to strengthen problem-solving and analytical thinking.