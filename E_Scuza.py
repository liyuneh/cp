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
    n , q = numbers()
    arr = numbers()
    arr.sort()
    quest = numbers()
    def right (ans, target) -> int:
        before = -1
        l , r = 0 , len(ans) - 1
        while l <= r :
            mid = l + (r - l ) // 2
            if ans[mid] <= target:
                before = mid
                l = mid + 1
            else:
                r = mid - 1
        return before
    pref = 0
    prefs = [0]
    for i in range(len(arr)):
        pref += arr[i]
        prefs.append(pref)
    res = []
    for i in range(len(quest)):
        res.append(prefs[right(arr,quest[i]) + 1])
    print(*res)

    return

for _ in range(test_cases()):
    solve()