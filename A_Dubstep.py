s = input()
s = s.split("WUB")
k = []
for i  in range(len(s)):
    if s[i] != '':
        k.append(s[i])
z = " ".join(k)
print(z)