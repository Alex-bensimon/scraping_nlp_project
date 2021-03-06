# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 15:48:23 2020

@author: Victor HENRIO
"""

import nlp
import tweet_scraping_scroll as tws
import sentiment_analysis as sent_analy
import pandas as pd
import crypto_benchmark as cryp_ben



def main():
    
    loc_file = tws.get_tweet_from_subject(10,"en","bitcoin",20,20,20)
    print("\n Nom du fichier :",loc_file,"\n")
    df = pd.read_csv("data/" +loc_file, sep="\\", names=['Content'])
    clean = nlp.clean_df(df)
    tweet_list = sent_analy.get_sentence_from_array(clean)
    sent_analy.get_sentiment_analyse(tweet_list)
    
    ## Benchmark crypto
    cryp_ben.benchmark(nb_crypto=5)




if __name__ == "__main__":
    main()