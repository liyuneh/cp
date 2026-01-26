import sys

t = int(input())
for _ in range(t):
    a, b, c = sorted(map(int, input().split()))
    
    if a == b == c:
        print("YES")
    elif b == c:
        print('YES' if b / 2 == a else 'NO')
    elif a == b:
        print('YES' if a + b == c or a + b + b == c or a + b == c / 2 else 'NO')
    else:
        print('YES' if b == 2 * a and a + b == c else 'NO')
