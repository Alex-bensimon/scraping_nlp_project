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

import pandas as pd 
import numpy as np

# Creation of the arrays that will fill the the csv file
content = np.array([])
tw_name = np.array([])

# Used to decide how much tweets we want to scrap
nb_of_tweets = 0

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
SCROLL_PAUSE_TIME = 2


while nb_of_tweets<100:
    
    #tweet_content = driver.find_elements_by_css_selector("article")
    #for e in tweet_content:
    #   print(e.text)
        
    tweet_content = driver.find_elements_by_css_selector("div[class='css-901oao r-18jsvk2 r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0']")
    for e in tweet_content:
        print("Tweet content : "+e.text)
        nb_of_tweets = nb_of_tweets + 1
        content = np.append(content,e.text.replace("\n"," "))
        
    # tweet names and @ are stored in the array tw_name but not used yet
    tweet_name = driver.find_elements_by_css_selector("a[class='css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-1wbh5a2 r-dnmrzs r-1ny4l3l']")
    for e in tweet_name:
        tw_name = np.append(tw_name,e.text)
        print(e.text)

    # Scroll down to bottom
    scroll(wait,1,2)
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)


# create the csv file named tweets.csv
np.savetxt("tweets.csv", content, delimiter="\\",fmt='%s',encoding="utf-8")


#%%

# NE T'OCCUPE PAS DE CA ENCORE C'EST UN BROUILLON

import pandas as pd 

df = pd.read_csv("tweets.csv", sep="\\")

print(df.info())