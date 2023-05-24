import asyncio
import aiohttp



async def get_page(session, url):
    try: 
        async with session.get(url) as response:
            return (response.status, url)
    
    except aiohttp.ClientError:
        result = 'aiohttp.ClientError'
        return (result, url)
    
    except: 
        result = 'error'
        return (result, url)
               

async def get_urls(urls):
    async with aiohttp.ClientSession() as session: 
        created_tasks = []
        for url in urls:
            created_tasks.append(asyncio.create_task(get_page(session, url)))
        results = await asyncio.gather(*created_tasks)
        return results

if __name__ == '__main__': 

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    urls = ['https://www.fit.vutbr.cz', 'https://www.szn.cz', 'https://www.alza.cz', 'https://office.com', 'https://aukro.cz']

    res = asyncio.run(get_urls(urls)) 

    print(res)
