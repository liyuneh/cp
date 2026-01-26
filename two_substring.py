n = input().upper()
if len(n) < 4 or 'AB' not in n or 'BA' not in n:
    print('NO')
else:
    if ('AB' in n and 'BA' in n[n.index('AB') + 2:]) or ('BA' in n and 'AB' in n[n.index('BA') + 2:]):
        print('YES')
    else:
        print('NO')