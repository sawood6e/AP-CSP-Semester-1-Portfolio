#Jan 7th, 2025
#Rock Paper Scissors

#Init
import random
playerScore = 0
computerScore = 0
#Functions
def rpsgame():
    global playerScore
    global computerScore
    while True:
        #Step 1 : Obtain the player's move
        print("Welcome to Rock, Paper, Scissors")
        print("What is your move?")
        player = input("Rock, Paper, Scissors, GO:")
        player = player.lower()
        #Step 2: Generate the computer's move
        computer = random.randint(1,3) #This function can generate a random integer from an interval
        if computer == 1:
            computer = "rock"
            print("The computer's move is rock")
        elif computer == 2:
            computer = "paper"
            print("The computer's move is paper")
        elif computer == 3:
            computer = "scissors"
            print("The computer's move is scissors")
        #Step 3: The outcome
        if player == "rock" and computer == "rock":
            print("It's a tie! You'll have to try again. ")
        elif player == "rock" and computer == "paper":
            print("Computer wins! Womp womp.")
            computerScore = computerScore + 1
        elif player == "rock" and computer == "scissors":
            print("Player wins! Hooray!")
            playerScore = playerScore + 1
        elif player == "paper" and computer == "rock":
            print("Player wins! Horray!")
            playerScore = playerScore + 1
        elif player == "paper" and computer == "paper":
            print("It's a tie! You'll have to try again.")
        elif player == "paper" and computer == "scissors":
            print("Computer wins! Womp womp.")
            computerScore = computerScore + 1
        elif player == "scissors" and computer == "rock":
            print("Computer wins! Womp womp.")
            computerScore = computerScore + 1
        elif player == "scissors" and computer == "paper":
            print("Player Wins! Hooray!")
            playerScore = playerScore + 1
        elif player == "scissors" and computer == "scissors":
            print("It's a tie! You'll have to try again.")
        print("Current score: Player: " + str(playerScore) + ", Computer: " + str(computerScore)) #Prints the current running score of all games played.
        playagain = input("Do you want to keep playing? Input yes or no: ")
        playagain = playagain.lower()
        if playagain == "no": #Allows player to stop playing
            print("Thanks for playing, see you next time!")
            break
        if playagain == "yes":
            print("Restarting program...")
#Main
rpsgame()
