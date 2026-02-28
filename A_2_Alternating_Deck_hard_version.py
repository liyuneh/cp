t = int(input())
for _ in range(t):
    n = int(input())
    ans = [1 + i for i in range(0, n + 4, 4)]
    # ans = [1] + ans 
    # print(ans)
    w1, b1 , w2, b2 = 0, 0, 0 ,0 
    for i in range(len(ans)):
        x = min(ans[i], n)
        if i % 2 == 0:
            w1 += (x // 2 ) + 1 if x % 2 == 1 else (x// 2 )
            b1 += (x // 2)
        else:
            w2 += (x // 2)
            b2 += (x // 2 ) + 1 if x % 2 == 1 else (x // 2)
        n -= ans[i]
        if n <= 0:
            break
    print(w1, b1, w2, b2)
    
    
