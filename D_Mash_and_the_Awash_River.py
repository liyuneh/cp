t = int(input())
for _ in range(t):
    n = input()
    if len(n) == 0:
        print(1)
    
    elif "**" in n or ">*" in n or "*<" in n or "><" in n :
        print(-1)
    else:
        if "<" in n and "*" not in n:
            x = n.rindex("<")
            print(max(len(n[:x+1]), len(n[x+1:])))
        elif "<" in n and "*" in n :
            x = n.rindex("*")
            print(max(len(n[:x+1]), len(n[x:])))

        else:
            print(len(n))
        