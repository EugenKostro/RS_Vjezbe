'''
def provjera_lozinke(lozinka):
    if len(lozinka) < 8 or len(lozinka) > 15:
        print("Lozinka mora sadržavati između 8 i 15 znakova")
        return
    
    veliko_slovo = any(char.isupper() for char in lozinka)
    ima_broj = any(char.isdigit() for char in lozinka)
    if not(ima_broj and veliko_slovo):
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
        return
    
    if "password" in lozinka.lower() or "lozinka" in lozinka.lower():
        print("Lozinka ne smije sadržavati riječi lozinka i password")
        return
    
    print("Lozinka je jaka")

lozinka = input("Unesite lozinku: ")
provjera_lozinke(lozinka)
'''
'''
def parni(lista):
    return [broj for broj in lista if broj % 2 == 0]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(parni(lista))
'''
'''
def duplikati(lista):
    return list(set(lista))

lista = [1,2,3,4,5,6,7,8,9,7,5,4,3,4]
print(duplikati(lista))
'''
'''
def brojanje_rijeci(tekst):
    rijeci = tekst.split()
    rezultat = {}

    for rijec in rijeci:
        if rijec in rezultat:
            rezultat[rijec] += 1
        else:
            rezultat[rijec] = 1
    
    return rezultat

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan"
print(brojanje_rijeci(tekst))
'''
'''
def grupiraj(lista):
    rezultat = {'parni': [], 'neparni': []}

    for broj in lista:
        if broj % 2 == 0:
            rezultat['parni'].append(broj)
        else:
            rezultat['neparni'].append(broj)
    return rezultat

lista = [1,2,3,4,5,6,7,8,9,10]
print(grupiraj(lista))
'''
'''
def obrni(rjecnik):
    return {vrijednost: kljuc for kljuc, vrijednost in rjecnik.items()}

rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}

print(obrni(rjecnik))
'''
'''
def prvi_i_zadnji(lista):
    return (lista[0], lista[-1])

lista = [1,2,3,4,5,6,7,8,9,10]
print(prvi_i_zadnji(lista))
'''
'''
def maks_i_min(lista):
    maks = lista[0]
    min_ = lista[0]
    for broj in lista[1:]:
        if broj > maks:
            maks = broj
        if broj < min_:
            min_ = broj
    return(maks, min_)

lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]
print(maks_i_min(lista))
'''
'''
def presjek(skup_1, skup_2):
    return {element for element in skup_1 if element in skup_2}

skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}
print(presjek(skup_1, skup_2))
'''
'''
def suglasnici_samoglasnici(tekst):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    rezultat = {'vowels': 0, 'consonants': 0}

    for znak in tekst:
        if znak in vowels:
            rezultat['vowels'] += 1
        elif znak in consonants:
            rezultat['consonants'] += 1

    return rezultat

tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(suglasnici_samoglasnici(tekst))
'''

