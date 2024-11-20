###Zadaci za vježbu - lambda izrazi, funkcije višeg reda i comprehension sintaksa

#Napišite korespondirajuće lambda izraze za sljedeće funkcije:
#Kvadriranje broja:
'''
def kvadriraj(x):
    return x**2

x = lambda x: x**2
print(x(5))

#Zbroji pa kvadriraj

def zbroji_pa_kvadriraj(a, b):
    return (a + b) ** 2

x = lambda a,b : (a+b) **2
print(x(5,6))

#Kvadriraj duljinu niza

def kvadriraj_duljinu(niz):
    return len(niz) ** 2

x = lambda niz: niz**2
print(x(1231))


#Pomnoži vrijednost s 5 pa potenciraj na x:

def pomnozi_i_potenciraj(x, y):
    return (y * 5) ** x

x = lambda x,y : (y*5) **x
print(x(3,3))


#Vrati True ako je broj paran, inače vrati None:

def paran_broj(x):
    if x % 2 == 0:
        return True
    else:
        return None
    
x = lambda x: True if x%2==0 else None
print(x(3))
'''

###Zadatak 2: Funkcije višeg reda
#Koristeći funkciju map , kvadrirajte duljine svih nizova u listi:
'''
nizovi = ["jabuka", "kruška", "banana", "naranča"]
kvadrirane_duljine = list(map(lambda x: len(x)**2, nizovi))
print(kvadrirane_duljine) # [36, 36, 36, 49]
'''

#Koristeći funkciju filter , filtrirajte samo brojeve koji su veći od 5:
'''
brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]
veci_od_5 = list(filter(lambda x: x>5, brojevi))
print(veci_od_5) # [21, 33, 45, 9, 10]
'''

#Koristeći odgovarajuću funkciju višeg reda i lambda izraz (bez comprehensiona), pohranite u varijablu
#transform rezultat kvadriranja svih brojeva u listi gdje rezultat mora biti rječnik gdje su ključevi
#originalni brojevi, a vrijednosti kvadrati tih brojeva:
'''
brojevi = [10, 5, 12, 15, 20]
transform = dict(map(lambda x: (x, x**2), brojevi))
print(transform) # {10: 100, 5: 25, 12: 144, 15: 225, 20: 400}
'''

#Koristeći funkcije all i map , provjerite jesu li svi studenti punoljetni:
'''
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
    {"ime": "Marko", "prezime": "Marković", "godine": 22},
    {"ime": "Ana", "prezime": "Anić", "godine": 21},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17},
    {"ime": "Mate", "prezime": "Matić", "godine": 18}
]
svi_punoljetni = all(map(lambda student: student["godine"] > 17, studenti))
print(svi_punoljetni) # False
'''

#Definirajte varijablu min_duljina koja će pohranjivati int . Koristeći odgovarajuću funkciju višeg reda
#i lambda izraz, pohranite u varijablu duge_rijeci sve riječi iz liste rijeci koje su dulje od
#min_duljina :
'''
rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
"pjesma", "otorinolaringolog"]
min_duljina = int(input("Unesite minimalnu duljinu riječi: "))
# min_duljina = 7
duge_rijeci = list(filter(lambda x: len(x) > min_duljina, rijeci))
print(duge_rijeci) # ['zvijezda', 'prijatelj', 'čokolada', 'otorinolaringolog']
'''

###Zadatak 3: Comprehension sintaksa
#Koristeći list comprehension, izgradite listu parnih kvadrata brojeva od 20 do 50:
'''
parni_kvadrati = [i **2 for i in range(20,51) if i % 2 == 0]
print(parni_kvadrati) # [400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764,
#1936, 2116, 2304, 2500]
'''

#Koristeći list comprehension, izgradite listu duljina svih nizova u listi rijeci , ali samo za nizove koji
#sadrže slovo a :
'''
rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
"pjesma", "otorinolaringolog"]
duljine_sa_slovom_a = [len(rijec) for rijec in rijeci if "a" in rijec]
print(duljine_sa_slovom_a) # [6, 3, 6, 8, 9, 8, 6, 17]
'''

#Koristeći list comprehension, izgradite listu rječnika gdje su ključevi brojevi od 1 do 10, a vrijednosti
#kubovi tih brojeva, ali samo za neparne brojeve, za parne brojeve neka vrijednost bude sam broj:
'''
kubovi = [{i: i**3 if i % 2 != 0 else i} for i in range(1, 11)]
print(kubovi) # [{1: 1}, {2: 2}, {3: 27}, {4: 4}, {5: 125}, {6: 6}, {7: 343}, {8: 8}, {9:
#729}, {10: 10}]
'''

#Koristeći dictionary comprehension, izgradite rječnik iteriranjem kroz listu brojeva od 50 do 500 s
#korakom 50, gdje su ključevi brojevi, a vrijednosti su korijeni tih brojeva zaokruženi na 2 decimale:
'''
korijeni = {i: round(i**0.5, 2) for i in range(50, 501, 50)}
print(korijeni) # {50: 7.07, 100: 10.0, 150: 12.25, 200: 14.14, 250: 15.81, 300: 17.32,
#350: 18.71, 400: 20.0, 450: 21.21, 500: 22.36}
'''

#Koristeći list comprehension, izgradite listu rječnika gdje su ključevi prezimena studenata, a vrijednosti
#su zbrojeni bodovi, iz liste studenti :

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
    {"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
    {"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
    {"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
    {"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
    {"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}
]
zbrojeni_bodovi = [{student["prezime"]: sum(student["bodovi"])}  for student in studenti]
print(zbrojeni_bodovi) # [{'Ivić': 152}, {'Marković': 127}, {'Anić': 55}, {'Petrić': 362},
#{'Ivić': 236}, {'Matić': 266}]
