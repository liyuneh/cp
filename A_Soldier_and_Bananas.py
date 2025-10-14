k, n, w = map(int, input().split())
Sum = 0
for i in range(1,w+1):
    Sum += (i * k)
z = Sum - n
if z >= 0:
    print(z)
else:
    print(0)