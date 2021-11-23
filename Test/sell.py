import requests
from bs4 import BeautifulSoup

url = "http://www.toysmile.com/"
web_data = requests.get(url)
soup = BeautifulSoup(web_data.text, 'html.parser')  
find_word = soup.find('title')
for i in find_word:
    print(i)