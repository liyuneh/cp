n = int(input())
for i in range(n):
    k = input()
    if (k[0] == 'b' and k[1] == 'c' ) or (k[0] == 'c' and k[1] == 'a'):
        print("NO")
    else:
        print("YES")