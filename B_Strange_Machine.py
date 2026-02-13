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
    colors = list(word())
    queries = numbers()
    ans = []

    for q in queries:
        count = 0
        i = 0
        if "B" not in colors:
            ans.append(q)
        else:
            while q != 0:
                if colors[i] == "B":
                    q = q//2
                else:
                    q = q - 1
                count += 1
                i = (i+1) % len(colors)
            ans.append(count)
    for a in ans:
        print(a)
    

    return

for _ in range(test_cases()):
    solve()