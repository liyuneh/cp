s = input()
k = input()
z = ""
for i in range(len(s)):
    if s[i] != k[i]:
        z += "1"
    else:
        z += "0"
print(z)