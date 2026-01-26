n = int(input())
for _ in range(n):
    s = input()
    unique = set(s)
    if len(unique) != len(s):
        print("NO")
        continue
    result = sorted([ord(c) for c in unique])
    min_val = result[0]
    max_val = result[-1]
    if (max_val - min_val) == len(result)- 1:
        print("YES")
    else:
        print("NO")