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
    n  = number()
    s = word()
    count = 1
    for i in range(len(s)- 1):
        if s[i] != s[i+1]:
            count += 1
    def subsequence(x):
        for i in range(len(x)-1):
            if x[i] == x[i+1]:
                return True
        return False
    if subsequence(s) and s[-1] != s[0]:
        print(count + 1)
    else:
        print(count)

    return


for _ in range(test_cases()):
    solve()
