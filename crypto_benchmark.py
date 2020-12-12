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
import matplotlib.pyplot as plt





def get_ordonate_crypto_list():
    crypto_list = []        
    crypto_page = requests.get("https://coinmarketcap.com/all/views/all/")
    soup = BeautifulSoup(crypto_page.text, 'lxml')    
    for a in soup.find_all('tr',  class_='cmc-table-row'):    
        crypto_list.append((a.find('a')).text)    
    return crypto_list



def normalize(lst):
    norm = [float(i)/sum(lst) for i in lst]
    return norm



def get_signe(number):
    if number < 0 :
        return -1
    else :
        return 1



def print_benchmark(list_norm_average_senti,liste_polarity):
    list_result = []
    for (crypto, polarity) in zip(list_norm_average_senti, liste_polarity):  
        list_result.append(polarity * crypto)
    print(list_result)
    return list_result



def Normalise(list_value):
    list_normalise = []
    mini = min(list_value)
    maxi = max(list_value)
    for ai in list_value:
        list_normalise.append(2*((ai - mini)/(maxi - mini))- 1)
    return list_normalise



def benchmark(nb_crypto):
    
    liste_polarity = []
    liste_average_senti = []
    liste_crypto = get_ordonate_crypto_list()
    print(liste_crypto[:nb_crypto])
    
    for crypto in liste_crypto[:nb_crypto]:
        loc_file = tws.get_tweet_from_subject(10,"en",crypto,20,20,20)
        print(loc_file)
        df = pd.read_csv("data/" +loc_file, sep="\\", names=['Content'])
        clean = nlp.clean_df(df)
        tweet_list = sent_analy.get_sentence_from_array(clean)        
        liste_average_senti.append(sent_analy.get_sentiment_analyse(tweet_list,schema=False))
        liste_polarity.append(get_signe(liste_average_senti[-1]))


    list_norm_average_senti = normalize(liste_average_senti)
    print_benchmark(list_norm_average_senti, liste_polarity)
    

    fig = plt.figure(figsize = (nb_crypto,5))
    ax = fig.add_axes([0,0,1,1])
    ax.set_title('Bilan analyse sentimental pour '+ str(nb_crypto) +" Crypto")
    ax.set_ylabel('Scores (Achat si sup à zéro Vente si inf)')
    crypto_sentiment = print_benchmark(list_norm_average_senti, liste_polarity)
    labels = liste_crypto[:nb_crypto]
    ax.bar(labels,crypto_sentiment)
    plt.show()
    




if __name__ == "__main__":
    benchmark(nb_crypto=3)

