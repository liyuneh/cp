from collections import defaultdict
s = input()
table = defaultdict(int)

for ch in s:
    table[ch] += 1
odd = False
count = 0
for val in table.values():
    count += (val // 2) * 2

    if val % 2 == 1:
        odd = True
x = count + 1 if odd else count
print(x == len(s))
