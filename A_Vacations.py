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
    nums = numbers()
    opt = [("", ""), ("", "c"), ("g", ""), ("g", "c")]
    stack = []
    for num in nums:
        a, b = opt[num]
#     dic = {0:[-1,-1], 1:[-1,1], 2:[1,-1], 3:[1,1]}
#     i = 0
#     count = 0
#     res = []
#     while i < len(nums):
#         if not res:
#             res.append(dic[nums[i]])
#         elif res:
#             a, b = res[-1]
#             c,d = dic[nums[i]]
#             if (c == d == -1 ) or (a == b == -1 or a == b == 1):
#                 res.append(dic[nums[i]])
#             elif a != c and d != b:
#                 res.append([c,d])
#             elif a == c and a != -1:
#                 res.append([-c,d])
#             elif a != c and b == d and b != -1:
#                 res.append([c,-d])
#             elif res[-1] == dic[nums[i]] :
#                 if a == 1:
#                     res.append([-a,b])
#                 else:
#                     res.append([c,-d])
        
#         i += 1
#     # print(res)
#     for i in range(len(res)):
#         a, b = res[i]
#         if a == b == -1:
#             count += 1
#     print(count)   

#     return

# for _ in range(test_cases(1)):
#     solve()