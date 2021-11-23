import json
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# driver = webdriver.Edge("D:\My Project\edgedriver_win64\msedgedriver.exe")
start_time = time.time()

def get_data(page_number):
    anime_list = []
    while True:
        api_url = f'https://api.bilibili.tv/intl/gateway/web/v2/ogv/index/items?buvid=7918C9CB-1802-8960-BAFC-7F4D0ED6A7AD52259infoc&csrf=28bc8f806e9033fbcc205b7f5b2a07a4&order=0&page={page_number}&pagesize=32&platform=web&s_locale=th_TH&season_type=1,4&timezone=GMT%2B07'
        print('1')
        get_web_data = requests.get(api_url)
        print('2')
        web_to_json = json.loads(get_web_data.text)
        print('3')
        # web_sort_json = json.dumps(web_data_json, indent=3, ensure_ascii=False) # ensure_ascii อ่านภาษาไทยออก
        # with open('api.json', 'w') as f:
        #     f.write(web_sort_json)
        # web_data_json = json.loads(web_sort_json)
        web_data = web_to_json['data']
        web_cards = web_data['cards']
        anime_list.append(web_cards)
        if not web_data['has_next']:
            break
        page_number += 1
    return anime_list
#     # for number_page in range(1, 30):
#     url = f'{api_data}{page_number}{api_data2}'
#     web_data = requests.get(url)
#     test = json.loads(web_data.text)
#     for i in test['data']['cards']:
#         for j in i:
#             print(i)
#     # return print(type(test['data']['cards']))
#     # return print((test['data']['cards'][0]['title']))
#     # soup = BeautifulSoup(web_data.text, 'html.parser')


page_number = 1
anime = get_data(page_number)
# print(type(anime))

# web_to_json = json.loads(str(anime))
# print(type(web_to_json))

# web_sort_json = json.dumps(anime, indent=3, ensure_ascii=False) # ensure_ascii อ่านภาษาไทยออก
with open('api raw.json', 'w') as f:
    json.dump(anime, f, indent=3)
#     f.write(web_sort_json)
print('finished')
# web_data = requests.get(url)
# soup = BeautifulSoup(web_data.text, 'html.parser')
# find_word = soup.find_all('p', {'class':'vertical-card__info_title'})
# for i in find_word:
#     i = str(i).replace('\n', "").replace('\t', "")
#     i = i.split('<p class="vertical-card__info_title">')[1]
#     print(i)
#     # i = i.get('src')
#     if i is not None:
#         print(i)
#         test.append(i)

# print(random.choice(test))

# with open('index.html', 'w',encoding='utf-8') as f:
#     f.write(web_data.text)

# print(web_data.text)
# driver.get(url)
# soup = BeautifulSoup(web_data.text, 'html.parser')
# find_word = soup.find_all('span', {'class':'highlight'})

# for i in find_word:
#     # i = str(i).split('<h2 class="woocommerce-loop-product__title">')[1][:-5]
#     print(i)
print("--- %s seconds ---" % (time.time() - start_time))
