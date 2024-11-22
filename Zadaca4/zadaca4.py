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

import asyncio

async def autorizacija():
    baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'email': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso123'}
    ]
    print("Autorizacija korisnika...")
    await asyncio.sleep(2)
    


async def autentifikacija():
    baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
    ]
    print("Provjera podataka...")
    await asyncio.sleep(3)
    for korisnik in baza_korisnika:
        if korisnik["korisnicko_ime"] and korisnik["email"] in baza_korisnika:
            return "Korisnik je u bazi"
        else:
            print(f'Korisnik {korisnik} nije pronađen')


asyncio.run(autentifikacija())