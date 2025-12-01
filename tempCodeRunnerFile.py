s =  input("Enter the string--> ")
k = int(input())

word = list(s)

l  = 0 
r = 0
while l < len(word) and r < len(word):
    if r - l + 1 == k:
        word[l] , word[r] = word[r], word[l]
        l += 2k
        r += k
    r += 1
print("".join(word))