 # -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 11:39:53 2020

@author: Victor HENRIO
"""

import time
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import numpy as np
import sys



def get_driver():
    print("create driver chrome")
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    return webdriver.Chrome(ChromeDriverManager().install())


def scroll(wait, nbr_of_scroll=1, time_to_sleep=15):
    for item in range(1): 
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        sleep(time_to_sleep)


def get_content_tweet(driver):
    content = np.array([])
    nb_tweet = 0
    tweet_content = driver.find_elements_by_css_selector("div[class='css-901oao r-18jsvk2 r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0']")
    for e in tweet_content:
        content = np.append(content,e.text.replace("\n"," "))
        nb_tweet += 1
    return content,nb_tweet 
    

    
def get_author_tweet(driver):
    tw_name = np.array([])
    tweet_name = driver.find_elements_by_css_selector("a[class='css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-1wbh5a2 r-dnmrzs r-1ny4l3l']")
    for e in tweet_name:
        tw_name = np.append(tw_name,e.text)
    return tw_name



def get_tweet_from_subject(nb_tweet = 10, language = "en", subject = "bitcoin",min_replies=20,min_faves=20,min_retweet=20):
    driver = get_driver()
    driver.get('https://twitter.com/search?f=live&q=lang%3A'+ language +'%20'+ subject +'%'+ str(min_replies) +'min_replies%3A20%'+ str(min_replies) +'min_faves%3A20%'+ str(min_replies) +'min_retweets%3A20&src=typed_query')
    wait = WebDriverWait(driver,15)
    SCROLL_PAUSE_TIME = 2   
    count = 0  
    full_content = np.array([])
    full_name = np.array([])  
    
    while count < nb_tweet:
            
        content,nb_scrap_tweet = get_content_tweet(driver)    
        full_content = np.append(full_content, content)

        full_name = np.append(full_name,get_author_tweet(driver))
        
        count += nb_scrap_tweet
        
        scroll(wait,1,2)
        time.sleep(SCROLL_PAUSE_TIME)
        loading_info(count, nb_tweet,"Scraping")                     
            
    
    full_name = full_name[2:]
    # create the csv file named tweets.csv
    file = str(count) + "tweets_on_" + subject +".csv"
    np.savetxt("data/" + file , full_content, delimiter="\\",fmt='%s',encoding="utf-8")
    np.savetxt("data/"+ str(count) + "name_tweets_on_" + subject +".csv", full_name, delimiter="\\",fmt='%s',encoding="utf-8")
    
    return file

def loading_info(prog,end,prefix):
    progression = (prog/end)*100
    sys.stdout.write(prefix + " ... %s%%\r" % (progression)+"\n")
    sys.stdout.flush()
    
 

if __name__ == "__main__":   

    get_tweet_from_subject(100,"en","bitcoin",20,20,20)
    
    
    


