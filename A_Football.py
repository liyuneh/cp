from collections import defaultdict
n = int(input())
table = defaultdict(int)
for i in range(n):
    k = input()
    table[k] += 1
max_key = max(table, key = table.get)
max_value = table[max_key]
print(max_key)