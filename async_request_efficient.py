import time
import aiohttp
import asyncio

import async_timeout

async def fetch_page(session, url):
    page_start_time = time.time()
    async with session.get(url) as response:
        print(f'Page took {time.time() - page_start_time} time')
        return response.status
    

async def get_multuple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks


loop = asyncio.get_event_loop()

urls = ['http://google.com' for i in range(50)]
start = time.time()
loop.run_until_complete(get_multuple_pages(loop, *urls))
print(f"All tasks took {time.time() - start}")

# -> 50 strings of google.com
# -> Then we pass them all as parameter in get_multuple_pages() along with loop that is runnig through as a task scheduler
# -> The loop is using a ClientSession just in case if we forget to pass it in or we forget to create one."Safe guard"
# -> Then, we are appending the COROUTINE created in the for loop into the tasks list syncronously one after another.
# -> Then, we gather them as one in grouped_tasks. -> It eventually AWAITS each task and only returns when they all are complete.
# -> The tasks are running individuallty in the event loop. -> This  is what gather dioes.
# -> return is executed when await is fully awaited
# -> PERFORMANCE IMPROVEMENT : NOT CREATING SESSION FOR EACH PAGE 

# ---------------

# If one task takes loooong time, we want to terminate the request
# If we are using loop.run_until_complete(), program wont finish until all the tasks are finished.
# We have to add some timeout. TErminate after X seconds
# In that case; use

async def fetch_page_timeout(session, url):
    page_start_time = time.time()
    async with async_timeout(20):
        async with session.get(url) as response:
            print(f'Page took {time.time() - page_start_time} time')
            return response.status