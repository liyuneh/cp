def leftbinary(z: int, k : list[int]) -> int:
    left, right = 0 , len(k) - 1
    ans = - 1
    while left <= right:
        mid = (left + right)//2
        if k[mid] < z:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans + 1
def rightbinary(z: int, k: list[int]) -> int:
    left, right = 0, len(k) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if k[mid] <= z:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans + 1


n = int(input())
h = list(map(int,input().split()))
h.sort()
p = int(input())
for i in range(p):
    left, right = map(int, input().split())
    a = rightbinary(right, h)
    c = leftbinary(left, h)
    print(a - c, end=" ") 