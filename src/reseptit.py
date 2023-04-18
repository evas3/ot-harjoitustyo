import random

class Recipes():
    def __init__(self):
        self.meal = ["keittoresepti", "sopparesepti", "soossiresepti"]
        self.dessert = ["kakkuresepti", "piirasresepti", "tortturesepti"]
        self.tiedosto = "ainesosasia.txt"
        print("Itse et osaa tehdä hyviä päätöksiä -minä voin päättää reseptit puolestasi")
        print("Tekeekö mieli kokata vai leipoa? Paina entteriä jos et osaa päättää")

    def welcome(self, sweet_or_salty):
        if sweet_or_salty.lower() == "m":
            return reseptit.sweet()
        elif sweet_or_salty.lower() == "s":
           return reseptit.salty()
        elif sweet_or_salty == "":
            choises = [reseptit.sweet, reseptit.salty]
            return random.choice(choises)()
        else:
            print()
            print("Yritetäänpä uudelleen")
            return reseptit.welcome()

    def sweet(self):
        print(reseptit.__str__(self.dessert))
        with open (self.tiedosto) as tiedosto:
            for rivi in tiedosto:
                print(rivi)
        reseptit.redo()

    def salty(self):
        print(reseptit.__str__(self.meal))
        with open (self.tiedosto) as tiedosto:
            for rivi in tiedosto:
                print(rivi)
        reseptit.redo()

    def redo(self):
        print()
        print("Haetko kenties jotakin muuta?")
        again = input("Valitaanko uusi resepti? Paina y-kirjainta niin yritetään uudelleen.")
        if again.lower() == "y":
            reseptit.welcome()
        print("Ole hyvä ja näkemiin!")
        
    def __str__(self, list):
        return random.choice(list)

if __name__ ==  "__main__":
    reseptit = Recipes()
    sweet_or_salty = input("Makeaa (paina m-kirjainta) vai Suolaista(paina s-kirjainta): ")
    reseptit.welcome(sweet_or_salty)
