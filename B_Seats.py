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
    s = list(word())
    if n == 1:
        print(1)
        return
    if all(i == '0' for i in s ):
        if n <= 3:
            print(1)
        else:
            print(2 + (n-4)// 3)
        return
    ans , zeros, found = 0 ,0 , False
    i = 0
    while i < len(s):
        if s[i] == '0':
            zeros += 1
        else:
            if (found):
                ans += (zeros // 3)
            else:
                ans += (zeros + 1)//3
                found = True
            zeros = 0
        i += 1
    ans += (zeros + 1)//3
    print(ans + s.count('1'))
    return

for _ in range(test_cases()):
    solve()