# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 11:39:53 2020

@author: Victor HENRIO
"""

import time
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def get_driver():
    print("create driver chrome")
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    return webdriver.Chrome(ChromeDriverManager().install())


def scroll(wait, nbr_of_scroll=1, time_to_sleep=15):
    for item in range(1): 
        print("scroll")
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        sleep(time_to_sleep)

        
driver = get_driver()
driver.get('https://twitter.com/search?q=lang%3Aen%20bitcoin&src=typed_query')  


wait = WebDriverWait(driver,15)
SCROLL_PAUSE_TIME = 5


    
while True:
    
    tweet_content = driver.find_elements_by_css_selector("article")
    for e in tweet_content:
        print(e.text)

        
    # Scroll down to bottom
    scroll(wait,1,10)

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)


