n = int(input())
for _ in range(n):
    k = int(input())
    arr = list(map(int, input().split()))
    Sum = sum(arr)
    print(0 - Sum)