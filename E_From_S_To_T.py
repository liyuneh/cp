from collections import Counter
n= int(input())
def subsequence(s,k):
    prev = -1
    ans = []
    for i in range(len(s)):
        for j in range(prev + 1 , len(k)):
            if s[i] == k[j]:
                ans.append(k[j])
                prev = j
                break
    return s == ''.join(ans)

for _ in range(n):
    s = input()
    t = input()
    p = input()

    if s == t:
        print("YES")
        continue
    if not subsequence(s,t):
        print("NO")
        continue
        
    counter_t = Counter(t)
    counter_p = Counter(p)
    counter_s = Counter(s)
    counter_s_p = counter_s + counter_p
    found = False
    for key  in counter_t:
        if counter_s_p[key] < counter_t[key]:
            print("NO")
            found = True
            break
    if not found :
        print("YES")