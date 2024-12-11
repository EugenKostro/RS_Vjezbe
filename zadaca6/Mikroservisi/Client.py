import asyncio
import aiohttp
import time

async def send_request(port):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://localhost:{port}/pozdrav') as response:
            return await response.json()
        
async def sekvencijalno():
    start_time = time.time()

    response1 = await send_request('http://localhost', 8081)
    print(f'Mikroservis1: {response1}')

    response2 = await send_request('http://localhost', 8082)
    print(f'Mikroservis2: {response2}')

    end_time = time.time()
    print(f'Sekvencijalno vrijeme: {end_time - start_time}')

async def konkurentno():
    start_time = time.time()

    responses = await asyncio.gather(   
        send_request('http://localhost', 8081),
        send_request('http://localhost', 8082)
    )

    for i, response in enumerate(responses, 1):
        print(f'Mikroservis {i} odgovor: {response}')
    
    end_time = time.time()
    print(f'Konkurentno vrijeme: {end_time - start_time}')

async def main():
    print("Sekvencijalno slanje: ")
    await sekvencijalno()

    print("Konkurentno slanje: ")
    await konkurentno()

if __name__ == '__main__':
    asyncio.run(main())