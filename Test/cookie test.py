from selenium import webdriver
from csv import DictReader

driver = webdriver.Edge("D:\My Project\edgedriver_win64\msedgedriver.exe")

url = 'https://10fastfingers.com/typing-test/english'
driver.get(url)

def get_cookies_values(file):
    with open(file, encoding='utf-8-sig', errors='ignore') as f:
        dict_reader = DictReader(f)
        list_of_dicts = list(dict_reader)
    return list_of_dicts

cookies = get_cookies_values('facebook.csv')

for i in cookies:
    driver.add_cookie(i)

driver.refresh()