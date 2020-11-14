# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 11:09:58 2020

@author: Alex
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

DRIVER_PATH = r'C:\Users\Alex\Documents\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://twitter.com/search?q=lang%3Aen%20bitcoin&src=typed_query')

sleep(5)

tweet_content = driver.find_elements_by_css_selector("div[class='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0']")
for e in tweet_content:
    print(e.text)
    
div = driver.find_elements_by_css_selector("div[class='css-901oao css-bfa6kz r-hkyrab r-1qd0xha r-a023e6 r-b88u0q r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0']")

for d in div:
    tweet_name = d.find_elements_by_css_selector("span[class='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0']")
    for tn in tweet_name:
        print(tn.text)