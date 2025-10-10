want = ["H", "Q", "9"]
s = input()
count = 0
for i in range(len(s)):
    if s[i] in want :
        count += 1
if count >= 1:
    print("YES")
else:
    print("NO")
    