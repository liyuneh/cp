s = int(input())
for _ in range(s):
    n , k = map(int, input().split())
    if k < n:
        print(k)
        continue
    want = k // (n - 1)
    got  = k * (k - 1)
    ans = 0
    if want * (n  - 1) == k:
        ans -= 1
    add = k - got
    ans += got + add + want
    print(ans)