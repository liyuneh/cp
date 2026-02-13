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
    first = numbers()
    second = numbers()
    third = numbers()
    res = [first, second, third]
    ans = []
    # mov = [[0,1],[1,0],[-1,0],[0,-1],[-1,-1], [1, -1], [-1, 1], [1, 1]]

    for i in range(len(res)):
        inside = []
        for j in range(len(res[0])):
            # for u , x in mov:
            #     ni = i + u
            #     nj = j + x
            #     if 0 <= ni < len(res) and 0 <= nj <= len(res[0]) - 1:

            x1 = res[i][j]
            x5 =  res[i-1][j] if i - 1 >= 0 else 0
            x2 = res[i+1][j] if i + 1 <= len(res) - 1 else 0
            x3 = res[i][j+1] if j + 1 <= len(res) - 1 else 0
            x4 = res[i][j-1] if j - 1 >= 0 else 0
            y = x1 + x2 + x3 + x4 + x5
            inside.append(y)
        ans.append(inside)
   
    matrix = []
    for i in range(len(ans)):
        num = []
        for j in range(len(ans[i])):
            if ans[i][j] % 2 == 1:
                num.append(0)
            else:
                num.append(1)
        matrix.append(num)
    for i in range(len(matrix)):
        print("".join(map(str,matrix[i])))
    


    return


for _ in range(test_cases(1)):
    solve()


