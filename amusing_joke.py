from collections import Counter
s1 = input().strip().upper()
s2 = input().strip().upper()
s3 = input().strip().upper()
k1 = s1 + s2

if Counter(k1) == Counter(s3):
    print("YES")
else:
    print("NO")
