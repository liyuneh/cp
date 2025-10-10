n  = int(input())
for i in range(n):
    k = int(input())
    if k & k - 1 == 0:
        print("NO")
    else:
        print("YES")