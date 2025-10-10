from collections import defaultdict

n = int(input())
for _ in range(n):
    k = int(input())
    arr = list(map(int, input().split()))
    
    table = defaultdict(int)
    for num in arr:
        table[num] += 1
    candidates = [num for num, count in table.items() if count >= 3]

    if candidates:
        print(max(candidates))  
    else:
        print(-1)
