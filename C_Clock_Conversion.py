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
    s = word()  # s is in "HH:MM" format
    hh, mm = map(int, s.split(":"))
    am_pm = "AM" if hh < 12 else "PM"
    hour = hh % 12
    if hour == 0:
        hour = 12
    print(f"{hour:02d}:{mm:02d} {am_pm}")

    return

for _ in range(test_cases()):
    solve()