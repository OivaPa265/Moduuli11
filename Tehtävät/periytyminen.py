class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):  # Renamed
        print(f"Kirjan tiedot: {self.nimi}, {self.kirjoittaja}, {self.sivumaara}")


class lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):  # Renamed variable
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):  # Renamed
        print(f"Lehden tiedot: {self.nimi}, {self.paatoimittaja}")


# Using the assignment's specific examples:
lehti1 = lehti("Aku Ankka", "Aki Hyyppä")
kirja1 = kirja("Hytti n:o 6", "Rosa Liksom", 200)

lehti1.tulosta_tiedot()
kirja1.tulosta_tiedot()