s = input()
prev = -1
for want in "hello":
    for i in range(len(s)):
        if s[i] == want and i > prev:
            prev = i
            break
    else:
        print("NO")
        exit()
print("YES")
