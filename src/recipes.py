import random
from tkinter import Tk
from graafinen_kayttoliittyma import UI


class Recipes():
    """Luokka jonka avulla päätetään reseptit.
    """


    def __init__(self):
        """Konstruktori luo listat resepteistä.
        """

        self.meal = ["./src/reseptit/nuudelit.txt",
                     "./src/reseptit/keitto.txt",
                     "./src/reseptit/hampurilaiset.txt"]
        self.dessert = ["./src/reseptit/mansikkakakku.txt",
                        "./src/reseptit/mustikkapiirakka.txt",
                        "./src/reseptit/kaaretorttu.txt"]


    def welcome(self, sweet_or_salty):
        """Toivottaa käyttäjän tervetulleeksi 
           määrittää valitaanko suolainen vai makea resepti.
        
        Args:
            sweet_or_salty: päätös kysymykseen yllä.
        """
        
        if sweet_or_salty == 1:
            return recepies.sweet()
        elif sweet_or_salty == 2:
            return recepies.salty()
        else:
            choises = [recepies.sweet, recepies.salty]
            return random.choice(choises)()
    

    def sweet(self):
        """Tulostaa leivonnaisen reseptin jos se on.
           Vanhaa reseptiä ei enää ehdoteta.
        """

        if self.dessert != []:
            chosen_dessert = random.choice(self.dessert)
            ui._show_recipe_view(chosen_dessert)
            self.dessert.remove(chosen_dessert)
            recepies.redo("")
        else:
            recepies.redo("sweet")


    def salty(self):
        """Tulostaa ruoan reseptin jos on.
           Vanhaa reseptiä ei enää ehdoteta.
        """

        print()
        if self.meal != []:
            chosen_meal = random.choice(self.meal)
            ui._show_recipe_view(chosen_meal)
            self.meal.remove(chosen_meal)
            recepies.redo("")
        else:
            recepies.redo("salty")


    def redo(self, doable):
        """Kysyy käyttäjältä valitaanko uusi resepti.

        Args:
            doable: kertoo jos reseptit ovat loppuneet
        """

        quit_if_0 = ui._show_redo_view(doable)
        if quit_if_0 == 0:
            window.destroy()
            print("You're welcome!")
        else:
            sweet_or_salty = ui.tklinter_welcome()
            recepies.welcome(sweet_or_salty)



if __name__ == "__main__":
    recepies = Recipes()
    window = Tk()
    window.title("What to cook?")
    ui = UI(window)
    sweet_or_salty = ui.tklinter_welcome()
    recepies.welcome(sweet_or_salty)
    window.mainloop() 