n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    if max(arr[:2]) < min(arr[2:])  or min(arr[:2]) > max(arr[2:]) :
        print("NO")
    else:
        print("YES")