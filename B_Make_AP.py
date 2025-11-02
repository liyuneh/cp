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
    a,b,c = numbers()
    if b - a == c - b:
        print("YES")
        return 
        print("YES")
    if (2 * b - c) > 0 and (2 * b - c) % a == 0:
        m1 = (2 * b - c) // a
        if m1 > 0:
            print("YES")
            return
    
    if (2 * b - a) > 0 and (2 * b - a) % c == 0:
        m2 = (2 * b - a) // c
        if  m2 > 0:
            print("YES")
            return
    
    if (a + c) > 0 and (a + c) % (2* b) == 0:
        m3 = ( a+ c) // (2 * b)
        if m3 > 0:
            print("YES")
            return
    print("NO")
    return

for _ in range(test_cases()):
    solve()