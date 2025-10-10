n = int(input())
numbers = list(map(int, input().split()))
even, odd = 0,0
for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        odd += 1
    else:
        even += 1
if even > odd:
    for i in  range( len(numbers) ):
        if numbers[i] % 2 != 0:
            print(i + 1)
else:
    for i in range( len(numbers) ):
        if numbers[i] % 2 == 0:
            print(i+ 1)