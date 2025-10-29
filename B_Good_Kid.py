n = int(input())
for _ in range(n):
    k = int(input())
    z = list(map(int, input().split()))
    z.sort()
    z[0] = z[0] + 1
    product = 1
    for i in range(len(z)):
        product *= z[i]
    print(product)