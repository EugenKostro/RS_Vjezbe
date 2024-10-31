#Zadatak 1 Validacija i provjera jakosti 
"""
def provjera_lozinke(lozinka):
    if not (8 <= len(lozinka) <= 15):
        print("Lozinka mora sadržavati između 8 i 15 znakova")
    elif not any(char.isupper() for char in lozinka):
        print("Lozinka mora sadržavati minimalno jedno veliko slovo")
    elif not any(char.isdigit() for char in lozinka):
        print("Lozinka mora sadržavati barem jedan broj")
    elif "password" == lozinka.lower() or "lozinka" == lozinka.lower():
        print("Lozinka ne smije sadržavati riječi 'password' i 'lozinka'")
    else:
        print("Lozinka je jaka")

# Unos lozinke
unos = input("Upišite lozinku: ")
provjera_lozinke(unos)
    
"""

#Zadatak 2 Filtriranje parnih iz liste
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

parni = list(filter(lambda x: x % 2 == 0, lista))

print(parni)
"""

#Zadatak 3 Uklanjanje duplikata u listi
'''
lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

lista = list(dict.fromkeys(lista))
print(lista)
'''

#Zadatak 4 Brojanje riječi u tekstu
'''
from collections import Counter

def brojac_rijeci(tekst):
    rijeci = tekst.split()
    brojac_rijeci = Counter(rijeci)
    for rijeci, broj in brojac_rijeci.items():
        print(f'"{rijeci}": {broj}')

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
brojac_rijeci(tekst)
'''

#Zadatak 5 Grupiranje elemenata po paritetu
'''
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

parni = []
neparni = []

for broj in lista:
    if broj % 2 == 0:
        parni.append(broj)
    else:
        neparni.append(broj)

print(f'"Parni: "{parni}" , Neparni: "{neparni}')
'''

#Zadatak 6 Obrnite riječi
'''
def obrni_rijecnik(rijecnik):
    obrnuti_rijecnik = {vrijednost: kljuc for kljuc, vrijednost in rijecnik.items()}
    return obrnuti_rijecnik

rijecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
obrni_rijecnik(obrni_rijecnik(rijecnik))
'''

#Zadatak 7 Napišite sljedeće funkcije
'''
#Funkcija koja vraća n-torku s prvim i zadnjim elementom liste u jednoj liniji koda

def prvi_i_zadnji(lista):
    print(f'({lista[0]}, {lista[-1]})')

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prvi_i_zadnji(lista)

#Funkcija koja vraća najmanji i najveći broj u listi bez funkcija min i max

def maks_i_min(lista):
    manji = lista[0]
    veci = lista[0]
    for broj in lista[1:]:
        if broj < manji:
            manji = broj
        if broj > veci:
            veci = broj
    print(f'{veci}, {manji}')

lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]
print(maks_i_min(lista))

#Funkcija koja prima dva skupa i vraća novi skup s elementima koji se nalaze u oba skupa

def presjek(skup_1, skup_2):
    skup = skup_1.intersection(skup_2)
    print(skup)

skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}
presjek(skup_1, skup_2)
'''

#Zadatak 8 Prosti brojevi
'''
def isPrime(broj):
    if broj <= 1:
        print(broj, "nije prost broj")
    else:
        for i in range(2, broj):
            if broj % i == 0:
                print(broj, "nije prost broj")
                return
        print(broj, "je prost broj")

broj = 3
isPrime(broj)
'''

#Zadatak 9 Pobroji samoglasnike i suglasnike
'''
def count_vowels_consonants(tekst):
    vowels = 0
    consonants = 0
    for char in tekst:
        if char in "aeiouAEIOU":
            vowels += 1
        elif char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            consonants += 1
    print(f'Samoglasnici: {vowels}, Suglasnici: {consonants}')

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."    
count_vowels_consonants(tekst)
'''