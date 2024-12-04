from shop.proizvodi import skladiste, dodaj_proizvod
from shop.narudzbe import napravi_narudzbu

proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

for proizvod in proizvodi_za_dodavanje:
    dodaj_proizvod(proizvod)

print("Proizvodi u skladistu: ")
for proizvod in skladiste:
    proizvod.ispis()

naruceni_proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 2},
    {"naziv": "Monitor", "cijena": 1000, "narucena_kolicina": 1}
]

narudzba = napravi_narudzbu(naruceni_proizvodi)
if narudzba:
    narudzba.ispis_narudzbe()