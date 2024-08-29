# Guessing Number game, random number input

import random
winning_number = random.randint(1, 100)
guess = 1
number = int(input("Guess a number b/w 1 to 100 : "))
game_over = False
                    
while not game_over:
    if number == winning_number:
        print(f"You Win, and you guessed in {guess} times")
        game_over = True
    
    else:
        if number < winning_number:
            print("Low")
            guess += 1
            number = int(input("guess number again : "))
        else:
            print("High")
            guess += 1
            number = int(input("guess number again : "))

