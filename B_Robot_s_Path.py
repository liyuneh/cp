n , k = map(int, input().split())
s = input()
if "#" not in s:
    print("YES")
else:
    count = 0
    ans = []
    for i in range(len(s)):
        if s[i] == "#":
            count += 1
        else:
            ans.append(count)
            count = 0
    ans.sort()
    if ans[-1] >= k:
        print("NO")
    else:
        print("YES")
        