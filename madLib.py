#Sadie Wood
#12/9/24
#Mad Libs Game

#Initialize

#Functions
def madLib():
    name=input("Please input a name: ")
    adjective1=input("Please input an adjective: ")
    pluralNoun=input("Please input a plural noun: ")
    place=input("Please input a place: ")
    ingVerb=input("Please input a verb ending in -ing: ")
    noun1=input("Please input a noun: ")
    spice=input("Please input a spice: ")
    adjective2=input("Please input an adjective: ")
    noun2=input("Please input a noun: ")
    foodItem=input("Please input a food item: ")
    adjective3=input("Please input an adjective: ")
    print(("Today, ") + name + (" decided to cook a ") + adjective1 + (" meal."))
    print(("First, they gathered all the ") + pluralNoun + (" from the ") + place + ("."))
    print(("They started by ") + ingVerb + (" the ") + noun1 + (" and then added a pinch of ") + spice + ("."))
    print(("The kitchen smelled ") + adjective2 + (", as the ") + noun2 + (" cooked."))
    print(("Finally, they served the dish with a side of ") + foodItem + ("."))
    print(("Everyone agreed it was the most ") + adjective3 + (" meal they had ever tasted!"))

#Main
madLib()
