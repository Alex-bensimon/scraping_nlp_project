# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 22:34:16 2020

@author: Victor HENRIO
"""

import nlp
import tweet_scraping_scroll as tws
import sentiment_analysis as sent_analy
import pandas as pd

import requests
from bs4 import BeautifulSoup




def get_ordonate_crypto_list():

    crypto_list = []        
    crypto_page = requests.get("https://coinmarketcap.com/all/views/all/")
    soup = BeautifulSoup(crypto_page.text, 'lxml')   
    
    for a in soup.find_all('tr',  class_='cmc-table-row'):    
        crypto_list.append((a.find('a')).text)
    
    return crypto_list


        


def benchmark(nb_crypto):
    
    liste_crypto = get_ordonate_crypto_list()
    print(liste_crypto)
    for crypto in liste_crypto[:nb_crypto]:
        loc_file = tws.get_tweet_from_subject(10,"en",crypto,20,20,20)
        print(loc_file)
        df = pd.read_csv("data/" +loc_file, sep="\\", names=['Content'])
        clean = nlp.clean_df(df)
        tweet_list = sent_analy.get_sentence_from_array(clean)
        info = sent_analy.get_sentiment_analyse(tweet_list,schema=False)
        print ("#"*10)
        print (info)





if __name__ == "__main__":
    benchmark(nb_crypto=2)