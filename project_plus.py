from bs4 import BeautifulSoup
import requests
import selenium
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome() # Опреляем браузер

fio = input().replace(" ", "%20") #input('ФИО...')
#Егоров Юрий Александрович
driver.get("https://zachestnyibiznes.ru/search?query="+fio)
time.sleep(7)

html = driver.page_source
print(html)

user_agent = {
    'user': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

a = {}
'''
def init():
    url = 'https://zachestnyibiznes.ru/search?query=Егоров%20Юрий%20Александрович'
    response = requests.get(url, headers=user_agent)
    soup = BeautifulSoup(response.content, 'html.parser')
    b = soup.find_all('span', {"class": "copy-string cursor c-black"})
    print(soup)
    
    for quote in b:
        a.append(quote.text)
        
        
    
init()
'''






