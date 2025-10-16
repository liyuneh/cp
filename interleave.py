a = [1, 3, 5, 7, 8]
b = [0, 3, 4, 5, 6]

def binarysearch(z: int, a: list[int]) -> int:
    # return first index i such that a[i] >= z, or len(a) if none
    left, right = 0, len(a) - 1
    ans = len(a)
    while left <= right:
        middle = left + (right - left) // 2
        if a[middle] >= z:
            ans = middle
            right = middle - 1
        else:
            left = middle + 1
    return ans

c = []
for x in b:
    idx = binarysearch(x, a)
    c.append(len(a) - idx)
print(c)
