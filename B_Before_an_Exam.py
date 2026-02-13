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
    d , n = numbers()
    sum1 = 0
    ans = []
    res = []

    for _ in range(d):
        mn , mx = numbers()
        sum1 += mn
        ans.append(mn)
        res.append(mx - mn)
    n -= sum1
    if n < 0:
         print("NO")
         return 
    if n == 0:
        print("YES")
        print(*ans)
        return 
        
    for i in range(len(ans)):
            if n - res[i] >= 0:
                ans[i] = ans[i] + (res[i])
                n -=  res[i]
            else:
                ans[i] = ans[i] + n
                n -= min(n , res[i])
    if n == 0:
        print("YES")
        print(*ans)
    else:
        print("NO")

    return

for _ in range(test_cases(1)):
    solve()