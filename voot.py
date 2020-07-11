from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import pandas as pd 
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser=webdriver.Chrome()
browser.get('https://www.hotstar.com/in/tv/list/popular-shows/t-5738_25_3?utm_source=search&utm_medium=Aw&utm_campaign=00_mindshareindia2-Hotstar-EM-Brand_SVOD_Bnd&utm_term=Hotstar')

res = browser.execute_script("return document.documentElement.outerHTML")

browser.maximize_window() 
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# time.sleep(10) 

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            match=True


browser.close()
  
soup = BeautifulSoup(res,'lxml')

data=soup.find('div',{'class':'resClass'})



show_list = list()

for item in data:
    name=data.find_all('span',{'class':'content-title ellipsise'})
    # subtitle=data.find_all('span',{'class':'subtitle'})
    for name_text in range(len(name)):
        show=name[name_text].text
        show_list.append(show) 
        show1=set(show_list)

df_bs = pd.DataFrame(show1,columns=['show1'])
df_bs.set_index('show1',inplace=True)
df_bs.to_csv('all_data1.csv')


print("seccesfull")







