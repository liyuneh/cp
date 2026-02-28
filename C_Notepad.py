t = int(input())
for _ in range(t):
    n = int(input())
    s = input() 
    if n <= 3:
        print("NO")
        continue
    # if n == 4:
    #     if s[:2] == s[2:]:
    #         print("YES")
    #     else:
    #         print("NO")
    #     continue
    flag = False
    for i in range(len(s)- 1):
        if s.count(s[i] + s[i+1]) >= 2:
            print("YES")
            flag = True
            break
    if not flag:
        print("NO")
            

