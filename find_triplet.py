n = int(input())
for _ in range(n):
    s = int(input())
    found = False
    for x in range(1, s - 1):
        if x % 3 == 0:
            continue
        for y in range(x + 1, s - x):
            if y % 3 == 0:
                continue
            z = s - x - y
            if z <= 0:
                continue
            if z % 3 != 0 and z != x and z != y:
                print("YES")
                print(x, y, z)
                found = True
                break
        if found:
            break
    if not found:
        print("NO")