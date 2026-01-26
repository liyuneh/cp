t = int(input())

for _ in range(t):
    count = 0
    n , m = map(int, input().split())
    x = input().strip()
    s = input().strip()
    max_operations = 10
    found = False
    while count <= max_operations:
        if s in x:
            found = True
            break
        x += x
        count += 1
    if found:
        print(count)
    else:
        print(-1)