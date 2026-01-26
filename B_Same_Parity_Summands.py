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
    n , k = numbers()
    if k == 1:
        print("YES")
        print(n)
        return 
    if k == n:
        print("YES")
        ans = [1]*k
        print(*ans)
        return
    if k > n or (k % 2 == 0 and n % 2 == 1) :
        print("NO")
        return
    if n % k == 0:
        ans = [n//k] * k
        print("YES")
        print(*ans)
        return
    if n % 2 == 1 and k %2 == 1 and k < n:
        ans = [1] * (k - 1)
        ans.append(n - ((k-1)*1))
        print("YES")
        print(*ans)
        return
    if n % 2 == 0 and k % 2 == 1:
        if n // 2 < k and k % 2 == 1:
            print("NO")
            return
        ans = [2] * (k-1)
        ans.append(n-((k-1)* 2))
        print("YES")
        print(*ans)
        return
    if n % 2 == 0 and k % 2 == 0 and n % k != 0:
        ans = [1]*(k-1)
        ans.append(n-((k-1)*1))
        print("YES")
        print(*ans) 
    return

for _ in range(test_cases()):
    solve()