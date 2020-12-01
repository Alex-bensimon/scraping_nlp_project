# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 09:54:44 2020

@author: Victor HENRIO
"""

import pandas as pd 
import nltk 
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
from spacy.lemmatizer import Lemmatizer
from nltk.stem.porter import *



def tokenisation(text):
    text_trait = text.replace("'"," ").replace("."," ")
    texte_token = nltk.sent_tokenize(text_trait.lower())
    all_words = [nltk.word_tokenize(sent) for sent in texte_token]
    return all_words

    
def delete_stop_word(array_of_word):
    stop_words = stopwords.words('english') + [",", ".", "!", "?", ";", "...", "'s", "--", "&","'","#","@","%"] + [k for k in range(100)]
    for i in range(len(array_of_word)):
        array_of_word[i] = [w for w in array_of_word[i] if w not in stop_words]
    return array_of_word


def porterStemmerFct(array_of_word):
    #print("\n","#"*40,"\n","\t PorterStemmerFct \n","#"*40,"\n")
    stemmer = PorterStemmer()
    singles = [stemmer.stem(plural) for plural in array_of_word[0]]
    return singles

def spacylemmatization(text):
    print("\n","#"*40,"\n","\t Spacy Lemmatization \n","#"*40,"\n")
    nlp = spacy.load('fr_core_news_sm')
    text_nlp = nlp(text)
    for token in text_nlp :
        print (token, token.lemma_)



def clean_df(df):
    #Pas réussi à append les listes dans le df
    #cleaned_df = pd.DataFrame(columns=["content"])
    cleaned_tab = []
    for index,tweet in df.itertuples():
        print("\n",tweet)
        token_tweet = tokenisation(tweet)
        print(token_tweet)
        tweet_without_stpw = delete_stop_word(token_tweet)
        print(tweet_without_stpw)
        porter_tweet = porterStemmerFct(tweet_without_stpw) 
        print("Porter : ",porter_tweet)
        #cleaned_df['content'] = porter_tweet
        #cleaned_df[index].append(porter_tweet)
        cleaned_tab.append(porter_tweet)
        print(cleaned_tab)
    
    return cleaned_tab


        
        
        
if __name__ == "__main__":
    
    df = pd.read_csv("data/1001tweets_on_bitcoin.csv", sep="\\", names=['Content'])
    clean = clean_df(df)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

"""

import string
import re

emoji_pattern = re.compile("["
         u"\U0001F600-\U0001F64F"  
         u"\U0001F300-\U0001F5FF" 
         u"\U0001F680-\U0001F6FF"  
         u"\U0001F1E0-\U0001F1FF"  
         u"\U00002702-\U000027B0"
         u"\U000024C2-\U0001F251"
         "]+", flags=re.UNICODE)

def clean_tweetdata(tweet):
 
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(tweet)
    tweet = re.sub(r':', '', tweet)
    tweet = re.sub(r'‚Ä¶', '', tweet)
    tweet = re.sub(r'[^\x00-\x7F]+',' ', tweet)
    tweet = emoji_pattern.sub(r'', tweet)
    filtered_tweet = [w for w in word_tokens if not w in stop_words]
    filtered_tweet = []
    for w in word_tokens:
        if w not in stop_words and w not in string.punctuation:
            filtered_tweet.append(w)
    return ' '.join(filtered_tweet)

for ind,i in enumerate(df['Content']):
    df['Content'][ind]=clean_tweetdata(i)
    
print(len(df['Content']))
"""