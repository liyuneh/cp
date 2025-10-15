n = int(input())
numbers = list(map(int, input().split()))
left , right = 0 , len(numbers) - 1
sereja_sum = 0
dima_sum = 0
count = 0
while left <= right:
    if count % 2 == 0:
        z = max(numbers[left] , numbers[right])
        sereja_sum += z
        count += 1
        if z == numbers[right]:
            right -= 1
        else:
            left += 1
    else:
        z = max(numbers[left] , numbers[right])
        dima_sum += z
        count += 1
        if z == numbers[right]:
            right -= 1
        else:
            left += 1
print(*[sereja_sum, dima_sum])