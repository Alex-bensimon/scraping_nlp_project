# Determine the polarity of a group of tweets

**Description** : We scrap the data from the social media Twetter to collect data about Bitcoin, the famous crypto-currency. 
After cleaning those data and place them in a pandas dataframe, our program is doing a sentimental analysis on each tweet and return the polarity.

## Authors

* **Alexadre Bensimon** 
* **Victor Henrio** 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

You need to clone the entire project on your device by doing this command :
```
* git clone https://github.com/Alex-bensimon/scraping_nlp_project.git
```
And then execute the main file by execute this command :
```
* main()
```
You will see the processus running and the result appears.

## Parameters

By changing the argument in the function "get_tweet_from_subject" you can personalise the way you scrap. 
You can play on the number of like, replies, retweets. 
You can also change the subject and the language of the scraping (and the sentimental analysis) by replacing "bitcoin" and "en".


### Prerequisites

You need to insatll Python version 2 at least to run beautifulsoup4 

We use all those library :

* selenium
* time
* Pandas
* Numpy
* sys
* nltk
* spacy
* textblob

## Built With

Python 3.7.6


## License

This project is licensed under the MIT License 

## Acknowledgments

* We thank Aymeric Laugel and Pierre Lazarz for their help and for sharing their passion with us.
