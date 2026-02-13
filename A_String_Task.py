t = input().lower()
k = []
for i in range(len(t)):
    if t[i] not in "aeiouy":
        k.append(t[i])
print("." + ".".join(k))