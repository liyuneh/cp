n = int(input())
for i in range(n):
    s = int(input())
    elem = list(map(int, input().split()))

    posible = True
    elem.sort()
    for i in range(1, s):
        if abs(elem[i] - elem[i-1]) > 1:
            posible = False
            break

    if posible :
        print("YES")
    else:
        print("NO")