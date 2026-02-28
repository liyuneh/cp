t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]

    left, right = 0, m - 1
    top, bottom = 0, n - 1

    total = 0

    while left < right and top < bottom:
        ans = []

        for j in range(left, right + 1):
            ans.append(grid[top][j])

        for i in range(top + 1, bottom + 1):
            ans.append(grid[i][right])

        for j in range(right - 1, left - 1, -1):
            ans.append(grid[bottom][j])

        for i in range(bottom - 1, top, -1):
            ans.append(grid[i][left])

        ans = "".join(ans)
        circular = ans + ans[:3]

        for i in range(len(ans)):
            if circular[i:i+4] == "1543":
                total += 1

        left += 1
        right -= 1
        top += 1
        bottom -= 1

    print(total)