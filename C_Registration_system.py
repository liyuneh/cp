n = int(input())

hash = {}
for i in range(n):
    c = input()
    if c not in hash:
        hash[c] = 1
        print("OK")
    else:
        print(f"{c}{hash[c]}")
        hash[c] += 1
