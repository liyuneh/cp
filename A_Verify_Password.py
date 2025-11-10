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
    n =number()
    s = word()
    ok = True
    for i in range(1,len(s)):
        if s[i-1].isalpha() and s[i].isdigit():
            ok = False
            break
        if s[i-1].isalpha() and s[i].isalpha() and ord(s[i-1]) > ord(s[i]):
            ok = False
            break
        if s[i-1].isdigit() and s[i].isdigit() and ord(s[i-1]) > ord(s[i]):
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")
    return

for _ in range(test_cases()):
    solve()