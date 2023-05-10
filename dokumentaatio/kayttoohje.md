# Käyttöohje
Projektin viimeisimmän version saa ladattua täältä: [Release]()

## Asennus ja käyttö
Käyttäjän tulee ensin asentaa vaaditut riippuvuudet käyttäen seuraavaa komentoa:

	poetry install

Ohjelma käynnistyy seuraavalla komennolla:

	poetry run invoke start


Tämän jälkeen käyttäjä seuraa ohjelman käyttäjälle antamia ohjeita.


Ensin käyttäjä valitsee haluaako hän suolaisen vai makean reseptin valitsemalla toisen napeista ja painamalla sitten OK.

Jos käyttäjä painaa vain OK, ohjelma arpoo palautetaanko makea vai suolainen resepti.

Ohjelma palauttaa arpomansa reseptin ja käyttäjä voi halutessaan lisätä tiedostoon huomautuksen kirjoittamalla sen tekstikenttään alareunassa ja painamalla OK.

Jos käyttäjä ei halua lisätä huomautusta, painaa hän vain OK.

Ohjelma kysyy haluaako käyttäjä kokeilla uutta reseptiä (jo tarjottua reseptiä ohjelma ei palauta uudelleen).

Jos käyttäjä valitsee ei tai painaa vain OK, ohjelman suoritus päättyy, jos käyttäjä valitsee jatka ja OK, ohjelma ns. aloittaa alusta muttei tarjoa jo palautettuja reseptejä.

Ohjelman voi keskeyttää ainoastaan valitsemalla tässä vaiheessa ei ja OK tai OK.
