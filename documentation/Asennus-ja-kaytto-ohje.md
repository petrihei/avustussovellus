# Asennusohje (alustava)

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

# Käyttöohje käyttäjälle (alustava)

* Rekisteröi käyttäjä
* Hae avustusta tai stipendiä
* Poista omia hakemuksia

# Käyttöohje adminille (alustava)

* Hyväksy, muokkaa tai poista avustushakemuksia
* Luo stipendejä
* Valitse stipendien saajat
* Muokkaa tai poista käyttäjiä