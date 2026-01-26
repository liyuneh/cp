a,b = map(int, input().split())
count = 0
while b >= a:
    count += 1
    a *= 3
    b *= 2
    
print(count)