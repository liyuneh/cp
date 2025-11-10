import sys
number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
test_cases = lambda inp=0: number() if not inp else inp

def solve():
    n = number()
    arr = numbers()
    sorted_arr = sorted(arr)
    if arr == sorted_arr:
        print("yes")
        print(1, 1)
        return
    l, r = 0, n - 1
    while l < n and arr[l] == sorted_arr[l]:
        l += 1
    while r >= 0 and arr[r] == sorted_arr[r]:
        r -= 1
    arr[l:r+1] = arr[l:r+1][::-1]
    if arr == sorted_arr:
        print("yes")
        print(l + 1, r + 1)
    else:
        print("no")

for _ in range(test_cases(1)):
    solve()
