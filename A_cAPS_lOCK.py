word = input()
if word.isupper() or (word[1:].isupper() and word[0].islower()) or len(word) == 1:
    word = word.swapcase()
print(word)
