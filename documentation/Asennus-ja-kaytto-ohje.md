### Asennusohjeet

* Forkkaa projekti ja lataa se paikalliseen versionhallintaan
```
https://github.com/petrihei/avustussovellus
```
* Luo Herokussa osoite sovellukselle
```
heroku create haluamasi-sovelluksen-osoite
```
* Lisää paikalliseen versionhallintaan tieto Herokusta
```
git remote add heroku https://git.heroku.com/haluamasi-sovelluksen-osoite.git
```
* Puske projekti Herokuun
```
git add .
git commit -m "Eka commit"
git push heroku master
```
* Luo ympäristömuuttuja Herokuun
```
heroku config:set HEROKU=1
```
* Lisää tietokanta Herokuun
```
heroku addons:add heroku-postgresql:hobby-dev
```
* Käynnistä tietokanta
```
heroku pg:psql
```
* Lisää tietokantaan Admin-käyttäjä
```
INSERT INTO account (name, username, password, role) VALUES ('Antti Admin', 'antti', 'admin', 'ADMIN');
```
* Käytä sovellusta


### Käyttöohjeet

# Käyttäjänä voit:

* Rekisteröityä
* Kirjautua
* Tehdä avustushakemuksen, jossa summa ja kuvaus
* Listata omat avustushakemuksen ja katsella niiden lisätietoja
* Poistaa omia avustushakemuksia
* Listata haettavat stipendit
* Hakea stipendiä

# Ylläpitäjänä voin:

* Listata kaikki avustushakemukset ja katsella niiden tarkempia tietoja
* Hyväksyä ja poistaa avustushakemuksia
* Muuttaa avustushakemuksen summaa
* Luoda uusia stipendejä
* Listata stipendejä
* Asettaa stipendin saajan
* Poistaa stipendin
* Listata stipendinhakijat stipendikohtaisesti
* Listata käyttäjät eri kriteereillä
* Tarkastella käyttäjän tietoja
* Muokata käyttäjän tunnusta ja salasanaa
* Poistaa käyttäjän