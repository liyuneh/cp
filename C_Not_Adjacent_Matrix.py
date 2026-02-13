import sys, math, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint
from heapq import heappush, heappop, heapify
from random import randint
Random = randint(100, 10**4)
Xor = lambda x:x ^ Random

number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yes_no = lambda condition: 'YES' if condition else 'NO'
test_cases = lambda inp=0: number() if not inp else inp

def solve():
    n = number()
    if n == 2:
        print(-1)
        return 
    res = [i  for i in range(1, n** 2 + 1)]
    odd = [res [i]  for i in range(len(res)) if res[i] % 2 == 1]
    even = [res[i] for i in range(len(res)) if res[i] % 2 == 0]
    res = odd + even

    ans = [res[i:i+n] for i in range(0, len(res), n)]
    for i in range(len(ans)):
        print(*ans[i])

    return


for _ in range(test_cases()):
    solve()
