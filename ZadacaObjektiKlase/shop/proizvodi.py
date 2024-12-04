class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        print(f"Naziv: {self.naziv}, Cijena: {self.cijena}, Dostupna kolicina: {self.dostupna_kolicina}")

skladiste = [
    Proizvod("Mobitel", 2000, 13),
    Proizvod("Slušalice", 100, 32)
]

def dodaj_proizvod(novi_proizvod):
    global skladiste
    skladiste.append(Proizvod(novi_proizvod["naziv"], novi_proizvod["cijena"], novi_proizvod["dostupna_kolicina"]))
    