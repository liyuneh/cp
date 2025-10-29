n = int(input())
for _ in range(n):
    k = int(input())
    arr = list(map(int, input().split()))
    stack = []
    count = 0
    for c in arr:
        if not stack:
            stack.append(c)
        else:
            if (c % 2 == stack[-1] % 2):  # same parity
                a = stack.pop()
                stack.append(a * c)
                count += 1
            else:
                stack.append(c)
    print(count)
