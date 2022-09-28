import aiohttp

import asyncio
import time

async def fetch_page(url):
    page_start = time.time()
    async with aiohttp.ClientSession() as session: # aiohttp.ClientSession() is a Connection Pool
        async with session.get(url=url) as response:
            print(f"Page took {time.time() - page_start}")
            return response.status


loop = asyncio.get_event_loop()


# If we want to run multiple requests
tasks = [fetch_page('http://google.com') for i in range(50)] # we will be creating 50 connection pools and stored. Then we move to next step => getting reponse

# Efficient way would be to create a session, and use all the urls in the same session -> async_request_efficient.py

# to run bunch of tasks together as a single task
start = time.time()
loop.run_until_complete(asyncio.gather(*tasks))
print(f"All tasks took {time.time() - start}")

# loop.run_until_complete(fetch_page('http://google.com'))