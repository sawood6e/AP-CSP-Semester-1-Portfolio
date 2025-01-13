#Sadie Wood
#Jan 9th, 2025
#Multiplication Quiz Game

#Initialize
import random
question_number = 0 #interger
wins = 0 #how many points the user has earned; integer
#Functions
def quiz():
    for index in range(5):
        num1 = random.randint(1,12) #integer
        num2 = random.randint(1,12) #integer
        global question_number
        global wins
        question_number = question_number + 1
        print("Question " + str(question_number) + " of 5:")
        print("What is " + str(num1) + " x " + str(num2) +"?")
        user_guess = int(input("Please input your guess: ")) #integer
        product = num1 * num2 #integer
        if user_guess == product:
            print("Correct!")
            wins = wins + 1
        else:
            print("Incorrect. The correct answer is " + str(product))
def game():
    print("Hello, Welcome to The Multiplication Quiz Game!" )
    quiz()
    print("Thanks for Playing! You got " + str(wins) + " of 5 question correct.")
#Main
game()
