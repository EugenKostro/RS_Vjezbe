###HTTP zahtjevi asinkroni python
import time
import requests
import aiohttp
import asyncio
'''
response = requests.get("https://catfact.ninja/fact")

#HTTP GET

print(response.text)
'''
#NE RADI
'''
async def main():
    async with aiohttp.ClientSession() as session:
        response = await session.get("https://jsonplaceholder.typicode.com/users")
        response_json = await response.json()
        print(response_json)
        return response_json

asyncio.run(main())
'''
'''
def send_request():
    response = requests.get("https://catfact.ninja/fact")
    odgovor = response.text
    print(odgovor)
    return response.text

for i in range(5):
    start_time = time.time()
    print(f"Šaljem zahtjev {i+1}...")
    send_request()

end_time = time.time()

print(f"Vrijeme izvršavanja je {end_time - start_time:.2f} sekundi")
'''
'''
async def main():
    async with aiohttp.ClientSession() as session:
        for i in range(5):
            print(f"Šaljem zahtjev {i+1}")
            response = await session.get("https://jsonplaceholder.typicode.com/users")
            response_json = await response.json()
            return response_json

asyncio.run(main())
'''
async def get_cat_fact(session):
    print(f"Šaljem zahtjev...")
    response = await session.get("https://jsonplaceholder.typicode.com/users")
    response_json = await response.json()
    print(response_json)

async def main():
    async with aiohttp.ClientSession() as session:
        lista_korutina = [get_cat_fact(session) for i in range(5)]
        rezultat = await asyncio.gather(*lista_korutina)
        print(rezultat)
        

asyncio.run(main())