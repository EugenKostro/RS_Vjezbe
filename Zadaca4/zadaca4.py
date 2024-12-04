###1. Definirajte korutinu koja će simulirati dohvaćanje podataka s weba. Podaci neka budu lista
#brojeva od 1 do 10 koju ćete vratiti nakon 3 sekunde. Listu brojeva definirajte comprehensionom.
#Nakon isteka vremena, u korutinu ispišite poruku "Podaci dohvaćeni." i vratite podatke. Riješite bez
#korištenja asyncio.gather() i asyncio.create_task() funkcija.
'''
import asyncio

async def korutina():
    podaci = [i for i in range(1, 11)]
    await asyncio.sleep(3)
    print(f'Podaci dohvaćeni... {podaci}')
   
asyncio.run(korutina())
'''

###2. Definirajte dvije korutine koje će simulirati dohvaćanje podataka s weba. Prva korutina neka vrati
#listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o korisnicima) nakon 3 sekunde, a druga
#korutina neka vrati listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o proizvodima) nakon 5
#sekundi. Korutine pozovite konkurentno korištenjem asyncio.gather() i ispišite rezultate. Program
#se mora izvršavati ~5 sekundi.
'''
import asyncio

async def korisnik():
    korisnici = [{'ime': 'Marko', 'prezime': 'Marković'}, {'ime': 'Petar', 'prezime': 'Perić'}]
    print('Dohvaćam podatke korisnika...')
    await asyncio.sleep(3)
    print('Podaci korisnika dohvaćeni.')
    return f'Korisnici: {korisnici}'

async def proizvod():
    proizvodi = [{'naziv': 'Banana', 'težina': '2 kile'}, {'naziv': 'Jabuka', 'težina': '4 kile'}]
    print('Dohvaćam podatke proizvoda...')
    await asyncio.sleep(5)
    print('Podaci proizvoda dohvaćeni.')
    return f'Korisnici: {proizvodi}'

async def main():
    rezultat = await asyncio.gather(korisnik(), proizvod())
    print(rezultat)

asyncio.run(main())
'''

###3. Definirajte korutinu autentifikacija() koja će simulirati autentifikaciju korisnika na
#poslužiteljskoj strani. Korutina kao ulazni parametar prima rječnik koji opisuje korisnika, a sastoji se
#od ključeva korisnicko_ime , email i lozinka . Unutar korutine simulirajte provjeru korisničkog
#imena na način da ćete provjeriti nalaze li se par korisnicko_ime i email u bazi korisnika. Ova
#provjera traje 3 sekunde.
'''
import asyncio

baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autorizacija(korisnik, unesena_lozinka):
    print("Autorizacija korisnika...")
    await asyncio.sleep(2)
    for entry in baza_lozinka:
        if entry['korisnicko_ime'] == korisnik['korisnicko_ime']:
            if entry['lozinka'] == unesena_lozinka:
                return "Autorizacija uspješna"
            else:
                return "Autorizacija neuspješna"

async def autentifikacija(korisnik):
    print("Autentifikacija korisnika...")
    await asyncio.sleep(3)
    for entry in baza_korisnika:
        if entry['korisnicko_ime'] == korisnik['korisnicko_ime'] and entry['email'] == korisnik['email']:
            rezultat = await autorizacija(entry, korisnik['lozinka'])
            return rezultat
    return f"Korisnik nije pronađen"

async def main():
    korisnik = {
        "korisnicko_ime": "mirko123",
        "email": "mirko123@gmail.com",
        "lozinka": "lozinka13"
    }
    rezultat = await autentifikacija(korisnik)
    print(rezultat)

asyncio.run(main())
'''

#4
'''
import asyncio
import random

async def provjeri_parnost(broj):
    await asyncio.sleep(2)
    if broj % 2 == 0:
        return f"Broj {broj} je paran"
    else:
        return f"Broj {broj} je neparan"

async def main():
    brojevi = [random.randint(1, 100) for i in range(10)]
    zadaci = [provjeri_parnost(broj) for broj in brojevi]
    rezultati = await asyncio.gather(*zadaci)

    for rezultat in rezultati:
        print(rezultat)

asyncio.run(main())
'''

import asyncio

async def secure_data(osjetljivi_podaci):
    await asyncio.sleep(3)
    enkriptirani_podaci = {
        'prezime': osjetljivi_podaci['prezime'],
        'broj_kartice': hash(osjetljivi_podaci['broj_kartice']),
        'CVV': hash(osjetljivi_podaci['CVV'])
    }
    return enkriptirani_podaci

async def main():
    osjetljivi_podaci_lista = [
        {'prezime': 'Ivić', 'broj_kartice': '1212345678', 'CVV': '123'},
        {'prezime': 'Marković', 'broj_kartice': '87687654321', 'CVV': '456'},
        {'prezime': 'Anić', 'broj_kartice': '111122223334', 'CVV': '789'}
    ]

    zadaci = [secure_data(podaci) for podaci in osjetljivi_podaci_lista]
    enkriptirani_podaci = await asyncio.gather(*zadaci)

    for podaci in enkriptirani_podaci:
        print(podaci)

asyncio.run(main())