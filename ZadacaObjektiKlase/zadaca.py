from datetime import datetime
#1
'''
class Automobil:
    def __init__(self, marka, model, godina, kilometraza):
        self.marka = marka
        self.model = model
        self.godina = godina
        self.kilometraza = kilometraza
    
    def ispis(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Godina: {self.godina}")
        print(f"Kilometraza: {self.kilometraza}")

    def starost(self):
        godinaAuta = datetime.now().year
        starost = godinaAuta - self.godina
        print(f"Automobil je {starost} godine/a star")

auto = Automobil("BMW", "M3", 2002, 2000000)

auto.ispis()
auto.starost()
'''

#2.
import math
'''
class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def zbroj(self):
        return self.a + self.b
    
    def oduzimanje(self):
        return self.a - self.b
    
    def mnozenje(self):
        return self.a * self.b
    
    def dijeljenje(self):
        return self.a / self.b
    
    def potenciranje(self):
        return self.a ** self.b
    
    def korijen(self):
        return math.sqrt(self.a), math.sqrt(self.b)
    
kalkulator = Kalkulator(2, 4)

print("Zbroj: ",kalkulator.zbroj())
print("Oduzimanje: ",kalkulator.oduzimanje())
print("Množenje: ",kalkulator.mnozenje())
print("Dijeljenje: ",kalkulator.dijeljenje())
print("Potenciranje: ",kalkulator.potenciranje())
print("Korijen: ",kalkulator.korijen())
'''

#3
'''
class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene) if self.ocjene else 0

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

# Kreiranje objekata klase Student
studenti_objekt = [Student(d["ime"], d["prezime"], d["godine"], d["ocjene"]) for d in studenti]

# Pronalaženje najboljeg studenta
najbolji = max(studenti_objekt, key=lambda student: student.prosjek())

# Ispis najboljeg studenta
print(f"Najbolji student je {najbolji.ime} {najbolji.prezime}, {najbolji.godine} {najbolji.prosjek()}")
'''

#4
'''
class Krug:
    def __init__(self, r):
        self.r = r
    
    def opseg(self):
        return 2 * math.pi * self.r
    
    def povrsina(self):
        return math.pi * (self.r ** 2)

krug = Krug(3)

print(f"Opseg: {krug.opseg()}")
print(f"povrsina: {krug.povrsina()}")
'''
#5
'''
class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa
    
    def work(self):
        print(f"Radim na poziciji: {self.pozicija}")

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department
    
    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}")

    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje
        print(f"Radnik {radnik.ime} ima placu {radnik.placa}")

radnik = Radnik("Anto", "Programer", 2000)
manager = Manager("Mario", "Menadžer", 3000, "IT")

radnik.work()
manager.work()

manager.give_raise(radnik, 1000)
'''

#6

