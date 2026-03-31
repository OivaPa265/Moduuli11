#Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
# Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja.
# Kirjoita luokkiin myös tarvittavat alustajat. Tee aliluokkiin metodi tulosta_tiedot, joka tulostaa kyseisen julkaisun kaikki tiedot.
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

# tekee luokan julkaisu jossa on nimi
class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

# tekee aliluojan kirja joka perii julkaislta nimen ja lisää kirjoittaja ja sivumäärän
class kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

# tulostaa kirjan
    def tulosta(self):
        print(f"Kirjan tiedot: {self.nimi}, {self.kirjoittaja}, {self.sivumaara}")

# tekee aliluokan lehti joka perii julkaisulta nimen ja lisää toisen nimen
class lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

# tulostaa lehden
    def tulosta(self):
        print(f"Lehden tiedot: {self.nimi}, {self.paatoimittaja}")

# antaa lehdelle nimen sekä päänimen
lehti1 = lehti("Aku Ankka", "Aki Hyyppä")

# antaa kirjalle nimen kirjoitajan sekä sivumäärän
kirja1 = kirja("Hytti n:o 6", "Rosa Liksom", 200)

#kutsuu tulostukset
lehti1.tulosta()
kirja1.tulosta()
