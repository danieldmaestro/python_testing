from random import choice
from emoji import emojize

class Word:
    def __init__(self, word):
        self._word = word
        self.temp_word = word
        self.word_blank = "_" * len(word)
        self.tries = 8

    @property
    def word(self):
        return self._word
    
    @property
    def word_len(self):
        return len(self._word)

    def hang_play(self, letter: str):
        self.tries -= 1
        if letter in self.temp_word:
            ind = self.temp_word.index(letter)
            self.word_blank = self.word_blank[:ind] + letter + self.word_blank[ind+1:]
            self.temp_word = self.temp_word[:ind] + "_" + self.temp_word[ind+1:]
            print(f"Great guess. You're good at this. You have {self.tries} tries left.\n")
        else:
            print(f"That's lame. This letter is not in the word. You have {self.tries} tries left.\n")


rand_word = choice(open('words.txt', 'r', encoding="utf-8-sig").readlines()).rstrip()

hang_word = Word(rand_word.lower())

print("Welcome to HANGMAN. Let's play.\n\nGuess each letter of the unknown word. You have 8 tries.\nIf you don't succeed, there's gonna be a noose around your neck.")
print(hang_word.word)

while hang_word.tries != 0:
    letter = input(f'Make your guess. Your {hang_word.word_len}-letter word is {hang_word.word_blank}:\n')
    hang_word.hang_play(letter)

    if "_" not in hang_word.word_blank:
        break

if "_" not in hang_word.word_blank:
    print(f"Congratulations. You win. Your word is {hang_word.word}")

else:
    print(f"Game over! Hang him!!")


