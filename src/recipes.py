import random


class Recipes():
    def __init__(self):
        self.meal = ["/home/evas/ot-harjoitustyo/src/nuudelit.txt",
                     "/home/evas/ot-harjoitustyo/src/keitto.txt",
                     "/home/evas/ot-harjoitustyo/src/hampurilaiset.txt"]
        self.dessert = ["/home/evas/ot-harjoitustyo/src/mansikkakakku.txt",
                        "/home/evas/ot-harjoitustyo/src/mustikkapiirakka.txt",
                        "/home/evas/ot-harjoitustyo/src/kaaretorttu.txt"]
        print("Can't make good decisions? I can!")
        print("Would you like to bake or cook? Press enter if you don't know.")

    def welcome(self, sweet_or_salty):
        if sweet_or_salty.lower() == "b":
            return recepies.sweet()
        elif sweet_or_salty.lower() == "c":
            return recepies.salty()
        elif sweet_or_salty == "":
            choises = [recepies.sweet, recepies.salty]
            return random.choice(choises)()
        else:
            print()
            print("Try that again")
            sweet_or_salty = str(
                input("Bake (press 'b') or cook (press 'c'): "))
            return recepies.welcome(sweet_or_salty)

    def sweet(self):
        print()
        with open(random.choice(self.dessert), "r") as file:
            for row in file:
                print(row)
        recepies.redo()

    def salty(self):
        print()
        with open(random.choice(self.meal), "r") as file:
            for row in file:
                print(row)
        recepies.redo()

    def redo(self):
        print()
        print("Anything else?")
        again = input(
            "Would you like to choose another recipe? Press 'y' to try again.")
        if again.lower() == "y":
            sweet_or_salty = str(
                input("Bake (press 'b') or cook (press 'c'): "))
            recepies.welcome(sweet_or_salty)
        else:
            print("You're welcome!")



if __name__ == "__main__":
    recepies = Recipes()
    SWEET_OR_SALTY = str(input("Bake (press 'b') or cook (press 'c'): "))
    recepies.welcome(SWEET_OR_SALTY)
    sweet_or_salty = str(input("Bake (press 'b') or cook (press 'c'): "))
    recepies.welcome(sweet_or_salty)
