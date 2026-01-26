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
    p = s
    consecutive = False
    index = 0
    for i in range(len(s)- 1):
        if s[i] == s[i+1]:
            consecutive = True
            index = i
            break
    new = ""
    if not consecutive:
        p += chr(ord('a') + ((ord(s[-1]) - ord('a') + 1) % 26))
        print(p)
    else:
        x = chr(ord('a') + ((ord(s[index]) - ord('a') + 1) % 26))
        new = s[:index+1] + x + s[index+1:]
        print(new)
    return

for _ in range(test_cases()):
    solve()