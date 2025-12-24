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

    count_odd = count_even = 0
    freq_odd = {}
    freq_even = {}
    for ch in arr:
        if ch % 2 == 0:
            count_even += 1
            freq_even[ch] = freq_even.get(ch, 0) + 1

        else:
            count_odd += 1
            freq_odd[ch] = freq_odd.get(ch, 0) + 1
    if (count_even % 2 == 0 and count_odd % 2 == 0):
        print("YES")
        return 
    found = False
    if count_odd % 2 == 1 and count_even % 2 == 1:
        for key in freq_even:
            if key + 1 in freq_odd or key - 1 in freq_odd:
                found = True
                break

        print("YES" if found else "NO")
        return 
    return

for _ in range(test_cases()):
    solve()