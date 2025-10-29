n = int(input())
num = n
ans = 0
multiplier = 1
while num > 0:
    d = num % 10
    num //= 10
    if num == 0 and d == 9:  
        ans += d * multiplier
    else:
        ans += min(d, 9 - d) * multiplier
    multiplier *= 10

print(ans)
