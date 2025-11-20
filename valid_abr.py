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
    s = word()
    abr = word()
    n , m = len(s), len(abr)
    l , r  = 0 , 0 
    while l < n and r < m:
        if s[l] == abr[r]:
            l , r = l + 1, r + 1
        elif (abr[r].isalpha() and abr[r] != s[l]) or abr[r] == '0':
            print("False")
            break
        else:
            x = 0
            while r < len(abr) and abr[r].isdigit():
                x = x * 10 + int(abr[r])
                r += 1
            l += x

    if l == len(s) and r == len(abr):
        print("True")
        return 
    return

for _ in range(test_cases(1)):
    solve()
