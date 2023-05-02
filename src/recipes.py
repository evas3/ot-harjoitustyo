import random


class Recipes():
    def __init__(self):
        self.meal = ["./src/reseptit/nuudelit.txt",
                     "./src/reseptit/keitto.txt",
                     "./src/reseptit/hampurilaiset.txt"]
        self.dessert = ["./src/reseptit/mansikkakakku.txt",
                        "./src/reseptit/mustikkapiirakka.txt",
                        "./src/reseptit/kaaretorttu.txt"]
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
        if self.dessert != []:
            chosen_dessert = random.choice(self.dessert)
            with open(chosen_dessert, "r") as file:
                for row in file:
                    print(row)
            self.dessert.remove(chosen_dessert)
            recepies.redo()
        else:
            print("No sweet options available")
            recepies.redo()

    def salty(self):
        print()
        if self.meal != []:
            chosen_meal = random.choice(self.meal)
            with open(chosen_meal, "r") as file:
                for row in file:
                    print(row)
            self.meal.remove(chosen_meal)
            recepies.redo()
        else:
            print("No salty options available")
            recepies.redo()

    def redo(self):
        while True:
            print()
            print("Anything else?")
            again = input(
                "Would you like to choose another recipe? Press 'y' to try again.")
            if again.lower() == "y":
                sweet_or_salty = str(
                    input("Bake (press 'b') or cook (press 'c'): "))
                recepies.welcome(sweet_or_salty)
                break
            else:
                print("You're welcome!")
                break



if __name__ == "__main__":
    recepies = Recipes()
    SWEET_OR_SALTY = str(input("Bake (press 'b') or cook (press 'c'): "))
    recepies.welcome(SWEET_OR_SALTY)