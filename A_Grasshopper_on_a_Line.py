t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if n % k != 0:
        print(1)
        print(n)
    else:
        n % k == 0:
        print(2)
        a = k - 1
        b = n - a
        print(a, b)
