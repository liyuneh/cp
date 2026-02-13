n = int(input())
t = list(map(int, input().split()))

prog = []
maths = []
pe = []

for i in range(n):
    if t[i] == 1:
        prog.append(i + 1)
    elif t[i] == 2:
        maths.append(i + 1)
    else:
        pe.append(i + 1)

w = min(len(prog), len(maths), len(pe))
print(w)

for i in range(w):
    print(prog[i], maths[i], pe[i])
