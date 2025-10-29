
def binaryinsert(z: int , arr:list[int]) -> int:
    left , right = 0 , len(arr) - 1
    while left <= right:
        middle = left +(right - left) // 2
        if arr[middle] <= z:
            left  = middle + 1
        else:
            right = middle - 1
    return right

n = int(input())

arr = sorted(list(map(int, input().split())))
q = int(input())
for _ in range(q):
    m = int(input())
    idx = binaryinsert(m, arr)
    print(idx + 1)


# 3 6 8 10 10 10  11