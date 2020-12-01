# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 09:54:44 2020

@author: Victor HENRIO
"""

import nlp as nlp
import pandas as pd
from textblob import TextBlob


def get_sentence_from_array(array_of_word):
    array_of_sentence = []
    for elem in array_of_word:
        sentence = ""
        for word in elem :
            sentence  = sentence + " " + word 
        array_of_sentence.append(sentence)
    
    return array_of_sentence



def get_sentiment_analyse(tweet_list):
    sentiments=[]
    subjectivity=[]
    
    for i in tweet_list:
        textblb = TextBlob(i)
        sentiments.append(textblb.polarity)
        subjectivity.append(textblb.subjectivity)
        
    pospol=0
    negpol=0
    nopol=0
    subcount=0
    for i in sentiments:
            if (i ==0):
                nopol+=1
            elif(i>0):
                pospol+=1
            elif(i<0):
                negpol+=1
    for i in subjectivity:
        if(i>0.5):
            subcount+=1
    print(' Zero polarities are '+ str(nopol))
    print(' Positive polarities are '+ str(pospol))
    print(' Negative polarities are '+str(negpol))
    print('Number of subjective tweets are : '+ str(subcount))
    
               
            
    
    


if __name__ == "__main__":
    
    df = pd.read_csv("data/1001tweets_on_bitcoin.csv", sep="\\", names=['Content'])
    clean = nlp.clean_df(df)
    tweet_list = get_sentence_from_array(clean)
    get_sentiment_analyse(tweet_list)
         



    






    
    