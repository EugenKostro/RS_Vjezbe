import asyncio
import aiohttp
import time
'''
#1
async def fetch_users(session):
    async with session.get("https://jsonplaceholder.typicode.com/users") as response:
        return await response.json()
    
async def main():
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        responses = await asyncio.gather(*[fetch_users(session) for i in range(5)])
        imena = [user['name'] for response in responses for user in response]
        email = [user['email'] for response in responses for user in response]
        username = [user['username'] for response in responses for user in response]

        print(f"Imena: {imena}")
        print(f"Emailovi: {email}")
        print(f"Usernameovi: {username}")

        end_time = time.time()
        print(f"Vrijeme: {end_time - start_time:.2f}")

asyncio.run(main())
'''

#2
'''
async def get_cat_fact(session):
    async with session.get("https://catfact.ninja/fact") as response:
        fact = await response.json()
        return fact['fact']
    
def filter(facts):
    return [fact for fact in facts if 'cat' in fact.lower()]

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [get_cat_fact(session) for i in range(20)]
        facts = await asyncio.gather(*tasks)
        filtered = filter(facts)
        print(f"Filtrirane činjenice o mačkama: {filtered}")

asyncio.run(main())
'''

#3

async def get_dog_fact(session):
    url = "https://dogapi.dog/api/v2/facts"
    async with session.get(url) as response:
        data = await response.json()
        return data['facts'][0]
    
async def get_cat_fact(session):
    url = "https://catfact.ninja/fact"
    async with session.get(url) as response:
        data = await response.json()
        return data['fact']
    
def mix_facts(dog_facts, cat_facts):
    return [dog_fact if len(dog_fact) > len(cat_fact) else cat_fact for dog_fact, cat_fact in zip(dog_facts, cat_facts)]

async def main():
    async with aiohttp.ClientSession() as session:
        dog_facts_tasks = [get_dog_fact(session) for i in range(6)]
        cat_facts_tasks = [get_cat_fact(session) for i in range(5)]

        dog_cat_facts = await asyncio.gather(*dog_facts_tasks, *cat_facts_tasks)

        dog_facts = dog_cat_facts[:5]
        cat_facts = dog_cat_facts[5:]

        mixed_facts = mix_facts(dog_facts, cat_facts)

        print("Miješane činjenice: ")
        for fact in mixed_facts:
            print(fact)

asyncio.run(main())