import aiohttp
import asyncio
from app.services.utils import random_name_generator


class AsyncCrawler:
    """
    Crawler using aiohttlp to downloads images  asynchronously.
    """

    def __init__(self, target_urls=[]):
        self.target_urls = target_urls

    @staticmethod
    async def fetch(client, url):
        async with client.get(url) as response:
            data = await response.read()
            ext = url.split(".")[-1]
            filename = random_name_generator(ext)
            with open(filename, 'wb') as out_file:
                out_file.write(data)

            return filename

    @staticmethod
    async def fetch_all(urls):
        async with aiohttp.ClientSession() as client:
            tasks = []
            for url in urls:
                tasks.append(
                    AsyncCrawler.fetch(
                        client,
                        url,
                    )
                )
            responses = await asyncio.gather(*tasks, return_exceptions=True)
            return responses

    def run(self):
        responses = asyncio.run(AsyncCrawler.fetch_all(self.target_urls))
        return responses
