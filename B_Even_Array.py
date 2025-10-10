def good(arr: list[int]) -> int:
    for i in range(len(arr)):
        count = 0
        if (i % 2 == 0 and arr[i] % 2 == 0) or (i % 2 != 0 and arr[i] % 2 != 0):
            return True
        else:
            return False
n = int(input())
for _ in range(n):
    k = int(input())
    z = list(map(int, input().split()))
    count = 0
    for i in range(k):
        if i % 2 == 0 and z[i] % 2 != 0:
            count += 1
        elif i % 2 != 0 and z[i] % 2 == 0:
            count += 1
    if good(z):
        print(0)
    elif count % 2 == 0:
        print(count // 2)
    else:
        print(-1)