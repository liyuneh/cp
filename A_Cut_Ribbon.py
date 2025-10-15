n,a,b,c = map(int, input().split())
count = 0
for i in range(3):
        
    if a + b == n:
        count += 1
    elif a + c == n:
        count += 1
    elif b + c == n:
        count += 1
if count == 0:
    print(count + 1)
else:
    print(count -1)