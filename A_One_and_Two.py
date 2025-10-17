n = int(input())
for _ in range(n):
    n = int(input())
    arr = list(map(int, input().split()))
    total = 1
    for num in arr:
        total *= num
    left_prod = 1
    found = False
    for i in range(len(arr)):
        left_prod *= arr[i]
        right_prod = total // left_prod
        if left_prod == right_prod:
            print(i + 1)
            found = True
            break
    if not found:
        print(-1)