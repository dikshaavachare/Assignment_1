def reverse_word(word): 
    new_word = ""
    for letter in word:
        new_word = letter + new_word
    return new_word
text = input("enter a word :")
print("reverse of word is:",reverse_word(text))


