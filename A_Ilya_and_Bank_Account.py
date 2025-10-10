n = int(input())
if n >= 0:
    print(n)
else:
    n_str = str(n)
    opt1 = int(n_str[:-1])
    opt2 = int(n_str[:-2] + n_str[-1])
    print(max(opt1,opt2))