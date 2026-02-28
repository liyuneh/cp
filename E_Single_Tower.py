n = int(input())
all_in_one = []
one = 0

for _ in range(n):
    full = list(map(int, input().split()))
    k = full[0]
    a = full[1:]
    all_in_one.append(a)
    one += k
total_block = []
for tow in all_in_one:
    total_block.extend(tow)

sorted_one = sorted(total_block)

freq = {v: i for  i , v in enumerate(sorted_one)}

s = 0
for tow in all_in_one:
    for i in range(len(tow) - 1):
        x = freq[tow[i]]
        y = freq[tow[i + 1]]
        if x + 1 != y:
            s += 1
c = n + s - 1
print(s, c)


