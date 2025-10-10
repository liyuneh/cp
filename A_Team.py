n = int(input())
count = 0
for i in range(n):
    s = input()
    s1 = s.count("1")
    if s1 >= 2:
        count += 1
print(count)