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
    ans = []

    for i in range(n):
        l , r = numbers()
        ans.append([l,r,i+1])
    ans.sort(key=lambda x:(x[0],-x[1]))
    for i in range(len(ans) - 1):
        if ans[i][1] >= ans[i+1][0]:
            print(ans[i+1][2])
            return 
    print(-1)
    
    return


for _ in range(test_cases(1)):
    solve()
