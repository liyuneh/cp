n, k = map(int, input().split())

def binarysearch(z: int, d: list[int]) -> int:
    left, right = 0, len(d) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if d[mid] <= z:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans + 1  

m = list(map(int, input().split()))
h = list(map(int, input().split()))
m.sort()

for x in h:
    print(binarysearch(x, m))