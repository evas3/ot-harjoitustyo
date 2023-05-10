# Reseptin arpoja
Sovellus auttaa käyttäjää päättämään mitä hän voisi kokata tai leipoa.
Käyttäjä kertoo halutessaan haluaako hän sovelluksen ehdottavan lounas reseptejä vai jälkiruokia.
Resepti valitaan satunnaisesta tiedoston käyttäjän antamien ehtojen rajoissa.
Käyttäjä voi halutessaan pyytää myös uutta reseptiä ja lisätä annetun reseptin loppuun oman huomautuksensa.


## Python versio
Sovellus on testattu Python-versiolla 3.8 eikä se välttämättä toimi vanhempien Python versioiden kanssa.


## Dokumentaatio

* [Release](https://github.com/evas3/ot-harjoitustyo/releases/tag/finalrelease)

* [Käyttöohje](https://github.com/evas3/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)

* [Arkkitehtuuri](https://github.com/evas3/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

* [Vaatimusmäärittey](https://github.com/evas3/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

* [Työaikakirjanpito](https://github.com/evas3/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)

* [Testaus](https://github.com/evas3/ot-harjoitustyo/blob/main/dokumentaatio/testaus.md)

* [Changelog](https://github.com/evas3/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)


## Asennus ja käyttö
Käyttäjän tulee ensin asentaa vaaditut riippuvuudet käyttäen seuraavaa komentoa:

	poetry install

Ohjelma käynnistyy seuraavalla komennolla:

	poetry run invoke start

Tämän jälkeen käyttäjä seuraa ohjelman käyttäjälle antamia ohjeita.
Ohjelmaa käytetään graafisen käyttöliittymän kautta. Käyttäjä siis painaa hiirellä nappia ja halutessaan kirjoittaa huomioille tarkoitettuun tekstikenttään.


## Muut komentorivikomennot
Testien suoritus seuraavalla komennolla:

	poetry run invoke test

Testikattavuusraportin generointi htmlcov-hakemistoon onnistuu komennolla:

	poetry run invoke coverage-report

Pylint määritelmien tarkastaminen toimii seuraavalla komennolla:

	poetry run invoke lint
