s = input()
l = s[1:-1]
if l == "":
    print(0)
else:
    print(len(set(l.split(", "))))
