n, m = map(int, input().split())
for i in range(n):
    for j in range(m):
        if i % 2 != 0 and i % 4 == 1:
            k = (m-1)* "." + "#"
        elif i % 2 != 0 and i % 4 == 3:
            k = "#" + (m-1)*"."
        else:
            k = m*"#"
    print(k)