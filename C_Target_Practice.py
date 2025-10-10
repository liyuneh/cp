score = [[1,1,1,1,1,1,1,1,1,1],
         [1,2,2,2,2,2,2,2,2,1],
         [1,2,3,3,3,3,3,3,2,1],
         [1,2,3,4,4,4,4,3,2,1],
         [1,2,3,4,5,5,4,3,2,1],
         [1,2,3,4,5,5,4,3,2,1],
         [1,2,3,4,4,4,4,3,2,1],
         [1,2,3,3,3,3,3,3,2,1],
         [1,2,2,2,2,2,2,2,2,1],
         [1,1,1,1,1,1,1,1,1,1]]


n = int(input())
for i in range(n):
    result = 0
    matrix = []
    for _ in range(10):
        row = list(input().strip())
        matrix.append(row)
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == "X":
                result += score[i][j]
    print(result)