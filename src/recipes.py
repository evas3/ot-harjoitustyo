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
        self._test_indicator = 0


    def main(self):
        """Luo tkinter ikkunan
        """
        self.window = Tk()
        self.ui_window = UI(self.window)

        self.window.title("What to cook?")
        sweet_or_salty = self.ui_window.tklinter_welcome()
        self.welcome(sweet_or_salty)
        self.window.mainloop()

    def welcome(self, sweet_or_salty):
        """Toivottaa käyttäjän tervetulleeksi 
           määrittää valitaanko suolainen vai makea resepti.

        Args:
            sweet_or_salty: päätös kysymykseen yllä.
        """

        if sweet_or_salty == 1:
            self._test_indicator = 1
            self.sweet()
        elif sweet_or_salty == 2:
            self._test_indicator = 2
            self.salty()
        else:
            choises = [self.sweet, self.salty]
            random.choice(choises)()

    def sweet(self):
        """Tulostaa leivonnaisen reseptin jos se on.
           Vanhaa reseptiä ei enää ehdoteta.
        """

        if self.dessert:
            self._test_indicator = 3.1
            chosen_dessert = random.choice(self.dessert)
            self.ui_window.show_recipe_view(chosen_dessert)
            self.dessert.remove(chosen_dessert)
            self.redo("")
        else:
            self._test_indicator = 3.2
            self.redo("sweet")

    def salty(self):
        """Tulostaa ruoan reseptin jos on.
           Vanhaa reseptiä ei enää ehdoteta.
        """

        print()
        if self.meal:
            self._test_indicator = 3.3
            chosen_meal = random.choice(self.meal)
            self.ui_window.show_recipe_view(chosen_meal)
            self.meal.remove(chosen_meal)
            self.redo("")
        else:
            self._test_indicator = 3.4
            self.redo("salty")

    def redo(self, doable):
        """Kysyy käyttäjältä valitaanko uusi resepti.

        Args:
            doable: kertoo jos reseptit ovat loppuneet
        """

        quit_if_0 = self.ui_window.show_redo_view(doable)
        if quit_if_0 == 0:
            self.window.destroy()
            print()
            print("You're welcome!")
            return "quit"

        sweet_or_salty = self.ui_window.tklinter_welcome()
        return self.welcome(sweet_or_salty)


if __name__ == "__main__":
    recipes = Recipes()
    recipes.main()
