n = int(input())
for _ in range(n):
    x, k = map(int, input().split())
    if x % 2 == 0 and k % 2 != 0 or x % 2 != 0 and k % 2 == 0:
        print(1)
        print(x)
    elif x % 2 == 0 and k % 2 == 0:
        print(2)
        print(3,x - 3)
    else:
        print(2)
        print(2, x - 2)