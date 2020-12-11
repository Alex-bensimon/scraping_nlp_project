# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 09:54:44 2020

@author: Victor HENRIO
"""

import nlp as nlp
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt


def get_sentence_from_array(array_of_word):
    array_of_sentence = []
    for elem in array_of_word:
        sentence = ""
        for word in elem :
            sentence  = sentence + " " + word 
        array_of_sentence.append(sentence)
    
    df = pd.DataFrame(array_of_sentence ,columns = ["tweet"])
    
    return df




def get_sentiment_analyse(tweet_list,schema=True):
    sentiments=[]
    subjectivity=[]
    
    for i in tweet_list["tweet"]:
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
    
    print("Average sentiment is: "+str(sum(sentiments)/len(sentiments))) 
    
    if schema :
        pols=['Neutral', 'Positive', 'Negative']
        polcount=[nopol,pospol,negpol]
        plt.pie(polcount, labels = pols,autopct='%1.2f%%')
    
    tweet_list['Sentiment']=sentiments
    tweet_list['Subjectivity']=subjectivity
    print(tweet_list.head())
    return (tweet_list)
    
    

                        
    
    


if __name__ == "__main__":
    
    df = pd.read_csv("data/1001tweets_on_bitcoin.csv", sep="\\", names=['Content'])
    clean = nlp.clean_df(df)
    df_tweet = get_sentence_from_array(clean)
    get_sentiment_analyse(df_tweet)
         



    






    
    