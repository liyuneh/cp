
dic = {
    'M': 1000, 'D':500, 'C': 100, 'L': 50, 'X': 10, 'V': 5 , 'I': 1
}
s = input("Enter the Roman number: ")
s = list(s)
Sum = 0
for i in range(0, len(s)-1):
    if dic[s[i]] >=  dic[s[i + 1]]:
        Sum  += dic[s[i]]
    else:
        Sum += dic[s[i + 1]]- dic[s[i]]
        i += 1
print(Sum )