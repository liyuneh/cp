z = input()
stack = []
c = 0

while c < len(z):
    if z[c] == '.':
        stack.append('0')
        c += 1
    elif z[c] == '-':
        if c + 1 < len(z) and z[c + 1] == '-':
            stack.append('2')
            c += 2
        elif c + 1 < len(z) and z[c + 1] == '.':
            stack.append('1')
            c += 2
        else:
            c += 1
    else:
        c += 1

print("".join(stack))

