n = int(input())
for _ in range(n):
    t = int(input())
    arr = input()
    left , right = 0, len(arr) - 1
    ans = t
    while left < right and arr[left] != arr[right]:
        ans -= 2
        left += 1
        right -= 1
    print(ans)