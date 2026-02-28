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

    x = str(n)[::-1]
    l , r = 0 , 0
    i = 0
    while x[i] == "0":
        l += 1
        i += 1
    z = i + 1
    for i in range(z, len(x)):
        if x[i] != "0":
            r += 1
    print(l + r)   
            

    return


for _ in range(test_cases()):
    solve()
