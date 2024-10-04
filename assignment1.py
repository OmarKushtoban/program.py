
import random

print("Welcome to a nice game of Rock Paper Scissors!")
print("______________________________________________\n")

choices = ("r", "p", "s")

playing = True

player_score = 0
computer_score = 0

howManyRounds = input("How many games would you like to play? ")
        
print(f"You will play {howManyRounds} games! ")



while playing:
    
    
    player = None
    computer = random.choice(choices)

        
    while player not in choices:
        
        
        player = input("Enter one of the following choices (rock, paper, scissors): ")

        print(f"Player: {player}")
        print(f"Computer: {computer}")


        if player == computer:
            print("It is a draw!!")
            

        elif player == "r" and computer == "s":
            print("You win!")
            print(f"Player score: {player_score}")
            player_score += 1

        elif player == "p" and computer == "r":
            print("You win!")
            print(f"Player score: {player_score}")
            player_score += 1

        elif player == "s" and computer == "p":
            print("You win")
            print(f"Player score: {player_score}")
            player_score += 1

        else:
            print("You lose!")
            print(f"Computer score: {computer_score}")
            computer_score += 1
           
        if not input("Play again? (y/n): ").lower() == "y":
            playing = False

            print("Thanks for playing!")
