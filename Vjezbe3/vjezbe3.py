###Asinkroni python
##Gather funkcija

import asyncio
'''
async def fetch_api_1():
    print('Dohvaćam podatke s API-ja 1...')
    await asyncio.sleep(2)
    print('Podaci s API-ja 1 dohvaćeni.')
    return {'api_1': 'uspješno'}

async def fetch_api_2():
    print('Dohvaćam podatke s API-ja 2...')
    await asyncio.sleep(3)
    print('Podaci s API-ja 2 dohvaćeni.')
    return {'api_2': 'uspješno'}

async def main():
    rezultat = await asyncio.gather(fetch_api_1(), fetch_api_2())
    print(rezultat)

asyncio.run(main())
'''
##Delay funkcija
'''
async def timer(name, delay):
    print(f"Počinje timer {name}...")
    for i in range(delay, 0, -1):
        print(f"Timer: {name}: {i} sec.")
        await asyncio.sleep(1)
    print(f"Kraj timera {name}...")

async def main():
    await asyncio.gather(timer("1", 5), timer("2", 3))
'''
#Taskovi
'''
async def fetch_api_1():
    print('Dohvaćam podatke s API-ja 1...')
    await asyncio.sleep(2)
    print('Podaci s API-ja 1 dohvaćeni.')
    return {'api_1': 'uspješno'}

async def fetch_api_2():
    print('Dohvaćam podatke s API-ja 2...')
    await asyncio.sleep(3)
    print('Podaci s API-ja 2 dohvaćeni.')
    return {'api_2': 'uspješno'}

async def main():
    task_1 = asyncio.create_task(fetch_api_1())
    task_2 = asyncio.create_task(fetch_api_2())

    podaci_1 = await task_1
    podaci_2 = await task_2

    print(f"Podaci s API-ja 1... {podaci_1}")
    print(f"Podaci s API-ja 2... {podaci_2}")
'''
#Konkurentno izvođenje 
'''
async def korutina(n):
    await asyncio.sleep(1)
    return f'Korutina {n} je završila'

async def main():
    tasks_comp = [await asyncio.create_task(korutina(i)) for i in range(1,6)]

    print(tasks_comp)
'''

asyncio.run(main())