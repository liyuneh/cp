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
    m, s = numbers()
    if m == 1 and s == 0:
        print(0,0)
        return
    
    if m == 0  or s == 0 or s > 9 * m:
        print(-1, -1)
        return
    
    mm = m
    z = s
    m_max = m
    m_min = m

    num = 0
    while s >= 9:
        num = num * 10 + 9
        s -= 9
        m_max -= 1
    if s > 0:
        num = num * 10 + s
        m_max -= 1
    
    mx = int(str(num) + m_max * '0')

    n = 0
    while z > 9:
        n = n * 10 + 9
        z -= 9
        m_min -= 1

    if m_min > 1:
        z -= 1
        n = (str(n) if n > 0 else "") + str(z) + (m_min - 2) * '0' + '1'
        n = int(n[::-1])
    else:
        n = n * 10 + z
        n = int(str(n)[::-1])

    print(n, mx)

for _ in range(test_cases(1)):
    solve()
