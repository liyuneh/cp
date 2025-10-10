n = int(input())
numbers = list(map(int, input().split()))
numbers.sort(reverse = True)
s_sum, d_sum  = 0, 0
for i  in range(n):
    if i % 2 == 0:
        s_sum += numbers[i]
    else:
        d_sum += numbers[i]

print(str(s_sum) + " " + str(d_sum))