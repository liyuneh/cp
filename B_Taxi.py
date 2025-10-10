n = int(input())
z = list(map(int, input().split()))
total = sum(z)
count = total // 4
remainder = total % 4
if remainder:
    print(count + 1)
else:
    print(count)

