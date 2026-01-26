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
    arr = numbers()

    if arr[0] > 25:
        print("NO")
        return 
    count25 , count50 = 0 , 0
    for x in arr:
        if x == 25:
            count25 += 1
        elif x == 50:
            if count25 == 0:
                print("NO")
                return
            count25 -= 1
            count50 += 1
        else:
            if count50 > 0 and count25 > 0:
                count50 -= 1
                count25 -= 1
            elif count25 >= 3:
                count25 -= 3
            else:
                print("NO")
                return
    print("YES")




    return

for _ in range(test_cases(1)):
    solve()