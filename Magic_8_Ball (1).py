#1/27/25
#Magic 8 Ball

#Init
import random
import time
magic8list = ["YES","Your outlook looks good","The vibes are positive","Very likely", "Probably","No", "Not looking good", "Low probability", "VERY unlikely", "The spirits are hinting no", "Ask again", "Maybe", "The answer is unclear", "The spirits are getting mixed signals","Not sure"] #15 possible responses. 5 positive, 5 negative, and 5 neutral responses.
i = 0
#Functions
def magic_8_ball():
    global i
    while i == 0:
        print("Welcome to Magic 8 Ball! Get ready to have your fortune read and all your questions answered.")
        question = input("Please enter a yes or no question: ")
        if question.endswith("?"):
            print("Shake...")
            time.sleep(1)
            print("Shake...")
            time.sleep(1)
            print("Shake...")
            time.sleep(1)
            print("Magic 8 Ball is thinking...Magic 8 Ball says...\n")
            time.sleep(2)
            print(random.choice(magic8list))
            again = input("\nWould you like to ask another question or try again? Enter yes(y) or no(n): ")
            if again == "n":
                print("\nGoodbye! Magic 8 Ball hopes all your pressing questions have been answered. See you next time!" )
                i = 1
        else:
            print("ERROR: Please enter a question (with punctuation)")

#Main
magic_8_ball()
