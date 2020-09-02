from random import randint

player_wins = 0
computer_wins = 0
winning_score = 3


while player_wins < winning_score and computer_wins < winning_score:
    print("PLAYER SCORE: {} COMPUTER SCORE {} ".format(player_wins,computer_wins))
    print("...ROCK...")
    print("...PAPER...")
    print("...SCISSORS...")

    player = input("(ENTER PLAYER 1's CHOICE :)").lower()
    if player == "quit" or player == "q":
        break
    rand_num = randint(0,2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
        
    print("Computer plays {}" .format(computer))    

    if player ==computer:
        print("It's a tie")
    elif player == "rock":
        if computer == "scissors":
            print("player wins")
            player_wins += 1 
        elif computer == "paper":
            print("computer wins")
            computer_wins += 1 
    elif player == "paper":
        if computer == "rock":
            print("player wins")
            player_wins += 1
        elif computer == "scissors":
            print("computer wins")
            computer_wins += 1
    elif player == "scissors":
        if computer == "paper":
            print("player wins")
            computer_wins += 1 
        elif computer == "rock":
            print("computer wins")
            computer_wins += 1
    else:
        print("something went wrong")

if player_wins > computer_wins:
     print("CONGRATS, YOU WON!")
elif player_wins == computer_wins:
     print("It's a tie")
else:
    print("OH NO :/ THE COMPUTER WON!")
        
print("FINAL SCORES: Player {} Computer: {}".format(player_wins,computer_wins))
