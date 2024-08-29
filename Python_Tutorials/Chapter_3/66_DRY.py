# Guessing Number game 

import random
winning_number = random.randint(1, 100)
guess = 1
number = int(input("guess a number b/w 1 to 100 : "))
game_over = False

while not game_over:
    if number == winning_number:
        print(f"You win, and you guessed in {guess} times")
        game_over = True
    else:
        if number < winning_number:
            print("low")
        else:
            print("high")

        guess += 1
        number = int(input("guess number again : ")) # DRY = don't repeat yourself. that's why we are using repeated statements in else block.
    
    