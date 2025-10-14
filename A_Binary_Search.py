n , k = map(int, input().split())
def binarysearch(z: int, d = list[int]) -> int:
    left, right = 0, len(d) - 1
    while left <= right:
        mid = (left + right) // 2
        if d[mid] == z:
            return mid
        elif d[mid] < z:
            left = mid + 1
        else:
            right = mid - 1
    return -1
m = list(map(int, input().split()))
h = list(map(int, input().split()))
for i in range(len(h)):
    if binarysearch(h[i], m) != -1:
        print("YES")
    else:
        print("NO")