from models import Admin

admin1 = Admin(
    ime="Eugen",
    prezime="Koštro",
    korisnicko_ime="eugenkostro",
    email="kostro.eugen@gmail.com",
    ovlasti=["dodavanje", "čitanje", "brisanje", "ažuriranje"]
)

admin2 = Admin(
    ime="Marko",
    prezime="Marić",
    korisnicko_ime="markomaric",
    email="markomaric@gmail.com",
    ovlasti=["dodavanje", "čitanje"]
)

print(admin1)
print(admin2)