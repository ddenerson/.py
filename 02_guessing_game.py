from random import randint

numbers = randint(1,10)
choose = None

while True:
    choose = input("Guess a number between 1 and 10:")
    choose = int(choose)
    if choose > numbers:
       print("To high, try again!")
    elif choose < numbers:
        print("To low, try again!")
    else:
        print("You guessed it! You won!")
        py_again = input("Do you want to play again? (y/n)")
        if py_again == "y":
            numbers = randint(1,10)
            choose = None
        else:
            print("Thank you for playing")
            break
