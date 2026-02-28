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
    arr = numbers()

    ans = float('inf')
    for i in range(n * 2):
        for j in range(i + 1, n * 2):
            new = []
            for k in range(n * 2):
                if k not in [i, j]:
                    new.append(arr[k])
            new.sort()
            cur = 0
            for t in range(1, len(new), 2):
                cur += (new[t] - new[t - 1])
            ans = min(ans, cur)
    print(ans)
    return


for _ in range(test_cases(1)):
    solve()
