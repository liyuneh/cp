n = int(input())
for _ in range(n):
    t = int(input())
    arr = list(map(int, input().split()))
    odd_sum = 0
    even_sum = 0
    for i in range(t):
        if arr[i] % 2 != 0:
            odd_sum += arr[i]
        else:
            even_sum += arr[i]
    if odd_sum % 2 == 0 and even_sum % 2 == 0:
        print("YES")
    else:
        print("NO")