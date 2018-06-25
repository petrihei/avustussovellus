## Käyttötapaukset

Käyttäjänä voin:

* Rekisteröityä
* Kirjautua
* Tehdä avustushakemuksen, jossa summa ja kuvaus
* Listata omat avustushakemuksen ja katsella niiden lisätietoja
* Poistaa omia avustushakemuksia
* Listata haettavat stipendit
* Hakea stipendiä

Ylläpitäjänä voin:

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

## Keskeisiä SQL-kyselyitä ja -komentoja

* Admin-käyttäjän luominen

```
INSERT INTO account (name, username, password, role) VALUES ('Antti Admin', 'antti', 'admin', 'ADMIN');
```

* Haku käyttäjistä, joilla ei ole hakemuksia

```
SELECT Account.id, Account.name FROM Account
LEFT JOIN Application ON Application.account_id = Account.id
WHERE (Application.approved IS null)
GROUP BY Account.id
HAVING COUNT(Application.id) = 0;
```

* Haku käyttäjistä, joilla ei ole hyväksyttyjä hakemuksia

```
("SELECT Account.id, Account.name FROM Account"
" LEFT JOIN Application ON Application.account_id = Account.id"
" WHERE (Application.approved != :approved OR Application.approved IS null)"
" GROUP BY Account.id").params(approved=True)
```

* Stipendinhakijoiden hakeminen

```
SELECT * FROM association;
```

* Tietyn käyttäjän hakemusten poisto ennen käyttäjän poistamista

```
("DELETE FROM Application WHERE Application.account_id = :acc_id").params(
acc_id=id)
```