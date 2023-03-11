import random
random_number = random.randint(1,10)

while True:   
    guess = input("Pick a number from 1 to 10:  ")
    guess = int(guess)
    if guess < random_number:
        print("TOO LOW")
    elif guess > random_number:
        print("TOO HIGH!")
    else:
        print("YOU WON!!!")
        play_again = input("Do yo want to play again? (y/n)  ")
        if play_again == "y":
            random_number = random.randint(1,10)
            guess = None
        else:
            print("Thanks for playing")
            break