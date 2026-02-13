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
    s = word()
    new_s = list(s)
    table = {}
    for i in range(26):
        table[chr(97 + i)] = chr((97+i))
    for _ in range(m):
        a, b = words()
        for key , val in table.items():
            if val == a:
                table[key] = b
            if val == b:
                table[key] = a
    differents = {}
    for key, val in table.items():
        if key != val:
            differents[key] = val
    for i in range(len(s)):
        if new_s[i] in differents:
            new_s[i] = differents[new_s[i]] 
    print("".join(new_s))

        
    return

for _ in range(test_cases(1)):
    solve()