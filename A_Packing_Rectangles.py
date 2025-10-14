w,h,n = map(int, input().split())
def good(x:int) -> bool:
    return (x/w) * (x/h) >= n
left , right = 0, 1
while not good(right):
    right *= 2
while right > left + 1:
    middle = (right  + left) // 2
    if good(middle):
        right = middle 
    else:
        left = middle 
print(right + 1) 