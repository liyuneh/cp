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
    s = word()
    l , r = - 1,-1
    for i in range(len(s)):
        if s[i] != '0':
            l = i
            break
    for i in range(len(s) - 1,- 1, -1):
        if s[i] != '0':
            r = i
            break
    ans = s[l:r+1]
    print("YES" if (ans == ans[::-1]) else "NO" )
    return


for _ in range(test_cases(1)):
    solve()
