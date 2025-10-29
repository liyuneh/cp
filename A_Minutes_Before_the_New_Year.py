n = int(input())
for _ in range(n):
    hour , min = map(int, input().split())
    ans = abs( (24 * 60)- (hour * 60 + min))
    print(ans)