matrix = []
for i in range(5):
    matrix.append(list(input().split()))
result = 0
for i in range(5):
    for j in range(5):
        if matrix [i][j] == "1":
            result += abs(2 - j)
            result += abs(2 - i)
print (result)