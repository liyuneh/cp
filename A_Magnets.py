n = int(input())
stack = ""
count = 0
for i in range(n):
    s = input()
    if stack != s:
        count += 1
    stack = s
print(count)