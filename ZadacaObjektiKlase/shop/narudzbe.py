from shop.proizvodi import skladiste, Proizvod

class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena
    
    def ispis_narudzbe(self):
        proizvodi_str = ", ".join([f"{p['naziv']} x {p['narucena_kolicina']}" for p in self.naruceni_proizvodi])
        print(f"Naruceni proizvodi: {proizvodi_str}, Ukupna cijena: {self.ukupna_cijena} eura")

narudzbe = []

def napravi_narudzbu(naruceni_proizvodi):
    if not isinstance(naruceni_proizvodi, list):
        print("Greška")
        return None
    if not all(isinstance(p, dict) for p in naruceni_proizvodi):
        print("Greška")
        return None
    if not all("naziv" in p and "cijena" in p and "narucena_kolicina" in p for p in naruceni_proizvodi):
        print("Greška")
        return None
    if not naruceni_proizvodi:
        print("Greška")
        return None
    
    ukupna_cijena = 0
    for p in naruceni_proizvodi:
        proizvod = next((s for s in skladiste if s.naziv == p["naziv"]), None)
        if not proizvod or proizvod.dostupna_kolicina < p["narucena_kolicina"]:
            print(f"Proizvod {p['naziv']} nije dostupan")
            return None
        ukupna_cijena += p["cijena"] * p["narucena_kolicina"]
    
    narudzba = Narudzba(naruceni_proizvodi, ukupna_cijena)
    narudzbe.append(narudzba)
    return narudzba