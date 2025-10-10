n = int(input())
p_m = list(map(int, input().split()))
q_m = list(map( int, input().split()))
p_w = set(p_m[1:] + q_m[1:])
z = set(range(1, n + 1))
if z.issubset(p_w):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")