import sys, math

number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
test_cases = lambda inp=0: number() if not inp else inp

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def solve():
    t = number()
    arr = numbers()

    for x in arr:
        r = math.isqrt(x)
        if r * r == x and is_prime(r):
            print("YES")
        else:
            print("NO")

for _ in range(test_cases(1)):
    solve()
