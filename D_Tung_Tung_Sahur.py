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
    p = word()
    s = word()
    left , right = [], []
    countl ,countr = 0 , 0
    l , r = p.index("L") if "L" in p else 0  , p.index("R") if "R" in p else 0
    for i in range(len(p)):
        if p[i] == "L":
            countl += 1
        elif p[i] != "L" and countl != 0:
            left.append((countl, l))
            countl = 0
            l = i
    if l  <=  i and countl != 0 :
        left.append((countl, l))
    
    for i in range(len(p)):
        if p[i] == "R":
            countr += 1
        elif p[i] != "R" and countr != 0:
            right.append((countr, r))
            countr = 0
            r = i
    if r <= i and countr != 0:
        right.append((countr, r))
        # print(countr)
    
    left1, right1 = [],[]
    countl1, countr1 = 0 , 0
    l1, r1 = s.index("L") if "L" in s else 0,s.index("R") if "R" in s else 0
    for i in range(len(s)):
        if s[i] == "L":
            countl1 += 1
        elif s[i] != "L" and countl1 != 0:
            left1.append((countl1, l1))
            countl1 = 0
            l1 = i
    if l1 <= i and countl1 != 0:
        left1.append((countl1, l1))
    for i in range(len(s)):
        if s[i] == "R":
            countr1 += 1
        elif s[i] != "R" and countr1 != 0:
            right1.append((countr1, r1))
            countr1 = 0
            r1 = i
    if r1 <= i and countr1 != 0:
        right1.append((countr1, r1))
    if len(left) != len(left1) or len(right) != len(right1):
        print("NO")
        return 
    flag1, flag2 = True, True
    for i in range(len(left)):
        if not (left[i][0] <= left1[i][0] <= 2 * left[i][0]) or  (left[i][1] > left1[i][1]):
            print("NO")
            flag1 = False
            return 
    for i in range(len(right)):
        if not (right[i][0] <= right1[i][0] <= 2 * right[i][0]) or (right[i][1] > right1[i][1]):
            print("NO")
            flag2 = False
            return 
    if flag1 and flag2:
        print("YES")

for _ in range(test_cases()):
    solve()




    # 6 1 15 19 9 13 12 6 7 2 10 4 1 14 11 14 14 13
