t = int(input())
for _ in range(t):
    n = int(input())
    ans = [1 + i for i in range(0, n + 4, 4)]
    # ans = [1] + ans 
    # print(ans)
    alice = 0
    bob = 0
    for i in range(len(ans)):
        if i % 2 == 0:
            alice += min(n ,ans[i])
        else:
            bob += (min(n, ans[i]))
        n -= ans[i]
        if n <= 0:
            break
    print(alice, bob)