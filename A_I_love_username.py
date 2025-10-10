n = int(input())
s = list(map(int, input().split()))
count = 0
max , min = s[0], s[0]
for i in range(1,len(s)):
    if s[i] > max :
        count += 1
        max = s[i]
    elif s[i] < min:
        count += 1
        min = s[i]
print(count)