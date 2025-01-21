from models import RestaurantOrder, Dish

jela = [
    Dish(id=1, naziv="Pizza", cijena=9),
    Dish(id=2, naziv="Burger", cijena=7)
]

stol_info = {"broj": 5, "lokacija": "dvorište"}

narudzba = RestaurantOrder(
    id = 101,
    ime_kupca = "Eugen Koštro",
    stol_info = stol_info,
    jela = jela,
    ukupna_cijena = sum(jelo.cijena for jelo in jela)
)

print(narudzba)