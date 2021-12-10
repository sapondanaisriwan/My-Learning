
from selenium import webdriver
import time
browser = webdriver.Edge('msedgedriver.exe')
browser.implicitly_wait(10)

url = 'https://10fastfingers.com/typing-test/english'
browser.get(url)

browser.find_element_by_id('CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection').click()
browser.maximize_window()

while True:
    text = browser.find_element_by_class_name('highlight').text + ' '
    text_box = browser.find_element_by_xpath('//*[@id="inputfield"]')
    text_box.send_keys(text)
    time.sleep(0.01)
