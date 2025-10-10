n = int(input())
for i in range(n):
    k = int(input())
    if k > 2 and k % 2 == 0:
        print(k // 2 - 1)
    elif k > 2 and k % 2 != 0:
        print((k + 1) // 2 - 1)
    else:
        print(0)