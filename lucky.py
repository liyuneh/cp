n = int(input())
for _ in range(n):
    s = input()
    if len(s) < 3:
        print("NO")
        continue
    first = s[:3]
    second = s[-3:]
    sum1 = sum(int(i) for i in first)
    sum2 = sum(int(i) for i in second)
    if sum1 == sum2:
        print("YES")
    else:
        print("NO")
