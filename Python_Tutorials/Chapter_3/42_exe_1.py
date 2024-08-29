# Number guessing game.
# Nested if-else function.

winning_number = 25
guess_number = int(input("Guess a number b/w 1 to 100 : "))
if guess_number == winning_number:
    print("you win !!")

else:
    if guess_number < winning_number:
        print("Too low")
#Nested if-else function
    else:
        print("Too High")