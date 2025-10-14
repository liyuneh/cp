n, k = map(int, input().split())

def binarysearch(z: int, d: list[int]) -> int:
    left, right = 0, len(d) 
    while left < right:
        mid =  left + (right - left)//2
        if d[mid] >=  z:
            right = mid
        else:
            left = mid + 1
    return left + 1
m = list(map(int, input().split()))
h = list(map(int, input().split()))
m.sort()

for x in h:
    print(binarysearch(x, m))