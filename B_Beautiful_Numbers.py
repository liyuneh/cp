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
    ans = list(str(n))
    total = sum(int(val) for val in ans)
    # print(total)
    if total <= 9:
        print(0)
        return 
    ans.sort(reverse = True)
    count = 0
    i = 0
    while total >= 9:
        total -= int(ans[i])
        count += 1
        i += 1
    print(count)
    return


for _ in range(test_cases()):
    solve()
