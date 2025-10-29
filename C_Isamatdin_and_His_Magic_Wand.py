import sys

number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
test_cases = lambda inp=0: number() if not inp else inp

def solve():
    t = number()
    for _ in range(t):
        n = number()
        arr = numbers()
        odd, even = 0, 0
        for i in range(n):
            if arr[i] % 2 == 0:
                even += 1
            else:
                odd += 1
            
        if odd > 0 and even > 0:
            arr.sort()
        print(*arr)
        
        

for _ in range(test_cases(1)):
    solve()
