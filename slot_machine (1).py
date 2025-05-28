#Slot Machine
#Init
import random
symbols = ["☆", "☆", "7", "💖", " ♫ ", "☔", "💖", " ♫ ", "☔"]
i = 0
tokens = 100
#Functions
def slot_machine():
    global i
    global tokens
    while i == 0:
        spin_quit = input("\nHello, Welcome to The Slot Machine!\nWould you like to spin(s) or quit(q): ")
        if spin_quit == "s" and tokens > 0:
            bet = input("How many tokens would you like to bet on this spin?: ")
            bet = int(bet)
            if bet <= tokens:
                tokens = tokens - bet
                slot1 = random.choice(symbols)
                slot2 = random.choice(symbols)
                slot3 = random.choice(symbols)
                print("\n" + slot1 + slot2 + slot3 + "\n")
                if slot1 == "7" and slot2 == "7" and slot3 == "7":
                    print("JACKPOT!!!")
                    tokens = tokens + bet*100
                    print("Number of tokens: " + str(tokens) + "\n")
                elif slot1 == slot2 and slot2 == slot3:
                    print("3 of a kind! That's a WIN!")
                    tokens = tokens + bet*10
                    print("Number of tokens: " + str(tokens) + "\n")
                elif slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
                    print("2 of a kind! That's a WIN!")
                    tokens = tokens + bet*3
                    print("Number of tokens: " + str(tokens) + "\n")
                else:
                    print("That's a LOSS :( Try again next time.")
                    print("Number of tokens: " + str(tokens) + "\n")
            else:
                reload = input("You have insufficiant tokens for this bet. Would you like to purchase 100 more tokens and continue playing? Yes(y) or No(n): ")
                if reload == "y":
                    tokens = tokens + 100
                    print("100 tokens have been added to your funds.")
                else:
                    print("Thank you for playing! Goodbye!")
                    i = 1
        elif spin_quit == "s":
            print("Number of tokens is insufficient. Come back another time.")
            i = 1
        elif spin_quit == "q":
            print("Thank you for playing! Goodbye!")
            i = 1

#Main
slot_machine()
