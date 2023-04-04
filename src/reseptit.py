#Tietokanta josta hataan reseptejä -pieni määrä erilaisia reseptejä (10) -hakusanat (suolainen/makea, luokka, arviointi, hinta, aika) sekä itse tulostettava resepti
#  Perus haku kondikseen -luokat!
# tarkempi haku
# käyttöliittymän parantaminen
# user input (aika arvion korjaaminen, hinta, arvostelu)
#lisätään reseptejä
# suosikit toiminnallisuus palauttaa 3 parasta (tehdyt tai arvostelu tai hinta)
"""luonne = input("1. Keksit ja pikkuleivät 2. Kakut ja piirakat 3. Muffinit ja mokkapalat, 3. Pullat ja letut 4. Muu")
    suodatus = input("Lajittelu a) Arvostelun mukaan b) Hinnan mukaan c) Uutuus tai vanha tuttu(d)")"""
"""luonne = input("1. Peruna, 2. Pasta, 3. Riisi, 4. Muu")
    suodatus = input("Lajittelu a) Arvostelun mukaan b) Hinnan mukaan c) Uutuus tai vanha tuttu(d)")"""
#hakukyselyn ohitus

class Reseptit():

    def __init__(self):
        pass
    def tervetuloa(self):
        #liibbalaaba ohjeet
        a = input("Makeaa (m) vai Suolaista(s): ")
        if a == "m":
            reseptit.makeaa()
        elif a == "s":
            reseptit.suolaista()
        elif a == "":
            reseptit.haku()
        else:
            pass
            #alusta, syöte ei vastaa od.
    def makeaa(self):
        pass
    def suolaista(self):
        pass
    def haku(self):
        pass
    def palautus(self):
        pass
        
reseptit = Reseptit()
a = input("Makeaa (m) vai Suolaista(s): ")
if a == "m":
    reseptit.makeaa()
elif a == "s":
    reseptit.suolaista()
elif a == "":
    reseptit.haku()
else:
    pass
    #alusta, syöte ei vastaa od