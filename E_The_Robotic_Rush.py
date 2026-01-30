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
    n, m, k = numbers()
    rob = sorted(numbers())
    spike = sorted(numbers())
    ins = word()

    current = 0
    left = []
    right = []
    deleted = set()

    for i in range(n):
        l = bisect_left(spike, rob[i])
        if l < m and spike[l] == rob[i]:
            heappush(left, (0, i))
            heappush(right, (0, i))
        else:
            if l - 1 >= 0:
                heappush(left, (spike[l - 1] - rob[i], i))
            if l < m:
                heappush(right, (spike[l] - rob[i], i))
        # print(l, left, right)
    # print(left, right)
    tot = n
    while right and current >= right[0][0]:
        deleted.add(heappop(right)[1])
        tot -= 1
    while left and current <= left[0][0]:
        if left[0][1] in deleted:
            heappop(left)
            continue
        deleted.add(heappop(left)[1])
        tot -= 1

    for i in ins:
        if i == "L":
            current -= 1
        else:
            current += 1
        while right and right[0][1] in deleted:
            heappop(right)
        while left and left[0][1] in deleted:
            heappop(left)
        while right and current >= right[0][0]:
            deleted.add(heappop(right)[1])
            tot -= 1
        while left and current <= left[0][0]:
            if left[0][1] in deleted:
                heappop(left)
                continue
            deleted.add(heappop(left)[1])
            tot -= 1
        # print(left, right, deleted, current, tot)
        print(tot, end=" ")
    print()
        
        

    return

for _ in range(test_cases()):
    solve()