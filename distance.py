import math
n = int(input())

for _ in range(n):
    l,r,d,u = map(int, input().split())
    p1 =  (-l, 0)
    p2 = (r,0)
    p3 = (0,-d)
    p4 = (0,u)
    side1 = math.dist(p1,p4)
    side2 =  math.dist(p2,p4)
    side3 = math.dist(p3,p1)
    side4 = math.dist(p3,p2)
    diag1 = math.dist(p1,p2)
    diag2 = math.dist(p3,p4)
    if  side1== side2==side3 ==side4 and  diag1 == diag2 :
        print("YES")
    else:
        print("NO")