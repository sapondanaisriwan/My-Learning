import time
from selenium import webdriver

url = 'https://www.facebook.com/'
driver = webdriver.Edge("msedgedriver.exe")
driver.get(url)

# with open('password.txt', 'r') as f:
#     lines = f.readlines()

# email = driver.find_element_by_name('email')
# email.send_keys(lines[0])
# print('email')
# time.sleep(5)
# password = driver.find_element_by_xpath('//*[@id="pass"]')
# password.send_keys(lines[1])
# print('password')
# time.sleep(3)

# button = driver.find_element_by_name('login')
# button.click()