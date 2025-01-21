from models import Knjiga, Izdavac

izdavac1 = Izdavac(naziv="BookRecords", adresa="Ulica Mate Parlova 3, Zagreb")

knjiga1 = Knjiga(
    naslov="Šegrt Hlapić",
    ime_autora="Ivana",
    prezime_autora="Brlić Mažuranić",
    broj_stranica=250,
    izdavac=izdavac1
)

print(knjiga1)