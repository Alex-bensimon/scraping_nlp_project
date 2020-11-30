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


def get_content_tweet():
    content = np.array([])
    nb_tweet = 0
    tweet_content = driver.find_elements_by_css_selector("div[class='css-901oao r-18jsvk2 r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0']")
    for e in tweet_content:
        print("Tweet content : "+e.text)
        content = np.append(content,e.text.replace("\n"," "))
        nb_tweet += 1
    return content,nb_tweet 
    

    
def get_author_tweet():
    tw_name = np.array([])
    tweet_name = driver.find_elements_by_css_selector("a[class='css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-1wbh5a2 r-dnmrzs r-1ny4l3l']")
    for e in tweet_name:
        tw_name = np.append(tw_name,e.text)
        print("Tweent Name :",e.text,"\n")
    return tw_name



def get_tweet_from_subject(nb_tweet = 10, language = "en", subject = "bitcoin",driver = get_driver()):
    driver.get('https://twitter.com/search?q=lang%3A'+ language +'%20'+ subject +'&src=typed_query')      
    wait = WebDriverWait(driver,15)
    SCROLL_PAUSE_TIME = 2   
    count = 0  
    full_content = np.array([])
    full_name = np.array([])
    while count < nb_tweet:
            
        content,nb_scrap_tweet = get_content_tweet()    
        full_content = np.append(full_content, content)

        full_name = np.append(full_name,get_author_tweet())
        
        count += nb_scrap_tweet
        
        scroll(wait,1,2)
        time.sleep(SCROLL_PAUSE_TIME)
        
        print("content :",content)
        print("nb_scrap_tweet",nb_scrap_tweet)
        
        
    
    full_name = full_name[2:]
    # create the csv file named tweets.csv
    np.savetxt("data/tweets.csv", content, delimiter="\\",fmt='%s',encoding="utf-8")

    



if __name__ == "__main__":   
    driver = get_driver()
    get_tweet_from_subject(10,"en","bitcoin",driver)
    
    
    


