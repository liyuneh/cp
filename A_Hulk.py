n = int(input())
res = []

for i in range(1, n + 1):
    if i % 2 != 0:
        res.append("I hate")
    else:
        res.append("I love")
    if i != n:
        res.append("that")
    else:
        res.append("it")

print(" ".join(res))
