s = input().lower()
s1 = input().lower()
flag = False
for i in range(len(s)):
    if ord(s[i]) < ord(s1[i]):
        print(-1)
        flag = True
        break
    elif ord(s[i]) > ord(s1[i]):
        print(1)
        flag = True
        break
if not flag:
    print(0)
