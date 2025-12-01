s =  input("Enter the string--> ")
k = int(input("Enter k--> "))

word = list(s)
i = 0
while i < len(word):
    l = i
    r = min(i + k - 1, len(word) - 1)

    while l < r:
        word[l], word[r] = word[r], word[l]
        l += 1 
        r -= 1
    i += 2 * k
        
print("".join(word))