word = input("Please enter a word: ")
vowel = "aeiou"

if word[0] in vowel:
    print("First letter is a vowel")
else:
    print("First letter is a consonant")