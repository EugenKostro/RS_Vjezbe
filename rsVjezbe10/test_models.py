from rsVjezbe10.models import Knjiga, Izdavac

izdavac1 = Izdavac(naziv="BookHouse", adresa="Mate Parlova 3, Zagreb")
knjiga1 = Knjiga(
    naslov="Šegrt Hlapić",
    ime_autora="Ivana",
    prezime_autora="Brlić Mažuranić",
    broj_stranica=200,
    izdavac=izdavac1
)
print(knjiga1)