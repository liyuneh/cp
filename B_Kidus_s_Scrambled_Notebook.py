t = int(input())
for _ in range(t):
    n = input()
    found = False
    for i in range(len(n)-1):
        if int(n[:i+1]) < int(n[i+1:]) and n[i+1] != "0":
            found = True
            print(n[:i+1], n[i+1:])
            break
    if not found:
        print(-1)
   
    
         
        
