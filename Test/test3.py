import json
import time
import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup
from requests import api
from requests.sessions import session
from selenium import webdriver

start_time = time.time()
# for page_number in range(1, 2):
#     api_url = f'https://api.bilibili.tv/intl/gateway/web/v2/ogv/index/items?buvid=7918C9CB-1802-8960-BAFC-7F4D0ED6A7AD52259infoc&csrf=28bc8f806e9033fbcc205b7f5b2a07a4&order=0&page={page_number}&pagesize=32&platform=web&s_locale=th_TH&season_type=1,4&timezone=GMT%2B07'
#     get_web_data = requests.get(api_url)
#     print(type(get_web_data.json()), type(get_web_data.text))

page_number = 1
api_url = f'https://api.bilibili.tv/intl/gateway/web/v2/ogv/index/items?buvid=7918C9CB-1802-8960-BAFC-7F4D0ED6A7AD52259infoc&csrf=28bc8f806e9033fbcc205b7f5b2a07a4&order=0&page={page_number}&pagesize=32&platform=web&s_locale=th_TH&season_type=1,4&timezone=GMT%2B07'

async def main():
    async with aiohttp.ClientSession() as session:
        test = await session.get(api_url, ssl=False)
        print(test.text)
    #     task = asyncio.ensure_future(get_web_data(session, page_number))
    #     print(task)
    #     test = await asyncio.gather(*task)
    # print(test)

# async def get_web_data(session, page_number):
#     anime_list=[]
#     return anime_list
    # async with session.get(api_url) as response:
    #     while True:
    #         raw_data = await json.loads(response.text)
    #         anime_list.append(raw_data)
    #         if not raw_data['has_next']:
    #             break
    #         page_number += 1
    #     return anime_list

if __name__ == "__main__":
    asyncio.run(main())

print("--- %s seconds ---" % (time.time() - start_time))
