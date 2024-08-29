# write a python program which will keep adding a stream of numbers inputted by the user. The adding stops as soon as user presses q key on the keyboard.
Bill = []
sum = 0 #sum variable starting with 0
while(True): # for infinite loop
    userInput = input("Enter the item price or press q to print Receipt: \n")
    if (userInput != 'q'):
        sum += int(userInput)
        Bill.append(userInput)
        print(f"Order Total so far is: {sum}")
    else:
        print(f"Your Bill Total is: {sum}. \nYour Purchase Summary:")
        for index, items in enumerate(Bill,start=1):
            print(f"({index}) {items}") 
            # enumerate(Bill, start=1) provides both the index (starting from 1) and the element for each iteration.
            # The f-string syntax (f"({index}) {items}") is used to format the output.
        print("ThankYou for Shopping. Visit Again!")

        break



