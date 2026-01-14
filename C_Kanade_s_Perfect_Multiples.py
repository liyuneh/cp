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
    n ,k = numbers()
    arr = numbers()
    arr.sort()
    seen = set(arr)
    heap = list(seen)
    heapify(heap)
    map = defaultdict(int)
    for i in range(n):
        map[arr[i]] = 1
    ans = []
    while seen :
        t = heappop(heap)
        if t not in seen:
            continue
        ans.append(t)
        seen.remove(t)

        cur = t
        while cur <= k :
            if not map[cur]:
                print(-1)
                return 
            if cur in seen:
                seen.remove(cur)
            cur += t
    print(len(ans))
    print(*ans)
    

    
    return

for _ in range(test_cases()):
    solve()