#10/18/24
#Name Generator

#Functions
def frogName():
    ans = input("frog (f) or toad (t)")
    if ans == "f":
        ans = input("mummy (m) or vampire (v)")
        if ans == "m":
            ans = input("sand (s) or rocks (r)")
            if ans == "s":
                print("You are a Desert Rain Frog!")
            else:
                print("You are a Cliff Chirping Frog!")
        if ans == "v":
            ans = input("quiet (q) or loud (l)")
            if ans == "q":
                print("You are a Golden Poison Frog!")
            else:
                print("You are a Marbled reed frog!")
    if ans == "t":
        ans = input("dragon (d) or wizard (w)")
        if ans == "d":
            ans = input("fire (f) or ash (a)")
            if ans == "f":
                print("You are a Fire-Bellied Toad!")
            else:
                print("You are a Dusky Toadlet!")
        if ans == "w":
            ans = input("howdy (how) or hello (he)")
            if ans == "how":
                print("You are a Texas Toad!")
            else:
                print("You are a Great Plains Toad!")
#Main
print("Welcome to the ultimate frog name generator!")
print("Answer the questions to find your frog name!")
frogName()

