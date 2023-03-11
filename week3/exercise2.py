word = input("Please insert a five-letter word: ").lower()
vowel = 'aeiou'
consonant = "cdfghjklmnpqrstvwxyz"
if not word.isnumeric():
    if len(word) == 5:
        if word[0] in vowel:
            print(f"{word[0]} is a vowel")
        elif word[0] in consonant:
            print(f"{word[0]} is a consonant")
        else:
            print(f"Invalid: {word[0]} is not an alphabet")

        if word[1] in vowel:
            print(f"{word[1]} is a vowel")
        elif word[1] in consonant:
            print(f"{word[1]} is a consonant")
        else:
            print(f"Invalid: {word[1]} is not an alphabet")
        
        if word[2] in vowel:
            print(f"{word[2]} is a vowel")
        elif word[2] in consonant:
            print(f"{word[2]} is a consonant")
        else:
            print(f"Invalid: {word[2]} is not an alphabet")

        if word[3] in vowel:
            print(f"{word[3]} is a vowel")
        elif word[3] in consonant:
            print(f"{word[3]} is a consonant")
        else:
            print(f"Invalid: {word[3]} is not an alphabet")

        if word[4] in vowel:
            print(f"{word[4]} is a vowel")
        elif word[4] in consonant:
            print(f"{word[4]} is a consonant")
        else:
            print(f"Invalid: {word[4]} is not an alphabet")
    else:
        print("Must be five letter word")
else: 
    print("A word, not number. Try dey read instruction")