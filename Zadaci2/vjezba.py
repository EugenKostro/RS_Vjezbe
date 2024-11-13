'''
def kvadriraj(x):
        return x ** 2

rez = kvadriraj(5)
#print(rez)

rez2 = lambda x: x ** 2
print(rez2(2))
'''
'''
def zbroj(x,y):
    return x+y

print(zbroj(5,6))
'''

'''
def pozdrav(ime = "Pero"):
    return ime

print(pozdrav())

print(pozdrav("Sanja"))
'''
'''
tekst = "Ovo je neki tekst"

veliki_tekst = lambda tekst: tekst.upper()

print(veliki_tekst(tekst))
'''
#funkcije više reda
'''
def fun(x):
    return x

def fun(lista, fun):
    return fun(lista)
'''
'''
def primijeni_na_sve(lista, funkcija):
    rezultat = []
    for element in lista:
        rezultat.append(funkcija(element))
    return rezultat

lista = [1, 2, 4, 3, 5]

def uvecaj_za_pet(broj):
    return broj + 5

nova_lista = primijeni_na_sve(lista, uvecaj_za_pet)

print(nova_lista)
'''
'''
def primijeni_na_sve(lista, funkcija):
    rezultat = []
    for element in lista:
        rezultat.append(funkcija(element))
    return rezultat

lista = [1, 2, 4, 3, 5]

nova_lista = primijeni_na_sve(lista, lambda broj: broj +5)

print(nova_lista)
'''

# MAP
'''
lista = [1, 2, 3, 4]

def kvadriraj(x):
    return x ** 2

lista_kvadriranih = list(map(kvadriraj,lista))

print(lista_kvadriranih)
'''
'''
print(list(map(lambda x,y : x +y, [1,2,3], [4,5,6])))
'''

#Filter
#NE RADI
'''
lista = [1,2,3,4,5,6,7,8,9,10]

def parni(lista):
    nova = []
    for element in lista:
        if element % 2 == 0:
            nova.append(element)
    return nova

lista_2 = filter(lambda x: x % 2 == 0, lista)

print(lista_2)
'''
'''
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godina_rodenja": 2000},
    {"ime": "Marko", "prezime": "Marković", "godina_rodenja": 1999},
    {"ime": "Ana", "prezime": "Anić", "godina_rodenja": 2003},
]
'''
#Klasično
#NE RADI
'''
def filtriraj_starije(studenti):
    nova = []
    for element in studenti:
        if studenti["godina_rodenja"] < 2000:
            nova.append(element)
    return nova

print(filtriraj_starije)
'''
#Lambda
'''
studenti_rodeni_prije_2000 = list(filter(lambda student: student["godina_rodenja"] < 2000, studenti))

print(studenti_rodeni_prije_2000)
'''
'''
def svi_parni(lista):
    for broj in lista:
        if broj % 2 != 0:
            return False
    return True

lista = [2, 4, 6, 8]
parnost = list(map(lambda broj : broj % 2 == 0, lista))

svi_parni = all(lista)

print(parnost)
'''

'''
#Klasično
kvadrati = []

for i in range(1, 11):
    kvadrati.append(i ** 2)

print(kvadrati) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#MAP

kvadrati = list(map(lambda x: x *+ 2, range(1, 11)))

#Comprehension

brojevi = [i for i in range(1, 11)]

print(brojevi)
'''
'''
nizovi = ["jabuka", "kruška", "banana", "naranča"]

novi_niz = [len(i) for i in nizovi]

print(novi_niz)
'''

#comprehension
'''
brojevi = [32, 54, 76, 12, 53, 67, 84, 11, 5, 6]
parni = [i**2 for i in brojevi if i % 2 == 0]

print(parni)
'''
#ako je paran stavi kvadrat, ako je neparan stavi kub
'''
paran_neparan = [i**2 if i % 2 == 0 else i**3 for i in brojevi]

print(paran_neparan)
'''
'''
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godina_rodenja": 2000},
    {"ime": "Marko", "prezime": "Marković", "godina_rodenja": 1998},
    {"ime": "Ana", "prezime": "Anić", "godina_rodenja": 2003},
]

#lista imena rođenih prije 1999
#comprehension

imena_rodenih_prije_99 = [student["ime"] for student in studenti if student["godina_rodenja"] < 1999]

print(imena_rodenih_prije_99)
'''
'''
def pomnozi_i_potenciraj(x, y):
    return (y * 5) ** x

pomnozi_i_potenciraj_lambda = (lambda x, y: (y*5)**x)

print(pomnozi_i_potenciraj_lambda(2, 3))
'''
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

print(svi_punoljetni) 
'''

#POPRAVITI
'''
kubovi = [if i%2 != 0 {i: i**3} else {i: i} for i in range(1,11)]

print(kubovi)
'''