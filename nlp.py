# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 10:17:42 2020

@author: Alex
"""


import pandas as pd 
import nltk 
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("tweets.csv", sep="\\", names=['Content'])
col = ['Content']
new_df = pd.DataFrame(columns=col)
i = 0

texte = df['Content'][0]
texte.lower().split()

texte = texte.lower()

sentence_list = sent_tokenize(texte)

print(sentence_list)

word_list = word_tokenize(texte)

print(word_list)

#%%
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
