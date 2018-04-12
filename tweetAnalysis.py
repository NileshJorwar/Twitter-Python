# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 10:49:27 2018

@author: niles
"""

from tweepy import OAuthHandler
from tweepy import API
import json
import re
from textblob import TextBlob

def main():
    # creating object of TwitterClient Class
    api = twitterClient()
    
    with open('python.json', 'r') as f:
        for line in f:
            tweet = json.loads(line) # load it as Python dict
            #import_processjson.preprocess(tweet['text'])     
            # saving text of tweet
            #parsed_tweet['text'] = tweet.text
            # saving sentiment of tweet
            
            analysis = TextBlob(clean_tweet(tweet))
            # set sentiment
            if analysis.sentiment.polarity > 0:
                return 'positive'
            elif analysis.sentiment.polarity == 0:
                return 'neutral'
            else:
                return 'negative'
            tweetList=get_tweet_sentiment(tweet.text)        
            print(tweetList)
            print(json.dumps(tweet, indent=4)) # pretty-print

    
def twitterClient():
    consumer_key="3YrMe9Y6q6jCUcTmvWnVZzjS2"
    consumer_secret="Y3fqkyAR2ZRw6Kin4vnzVd2QOnMC1DwLnWks3huO8wPpDHSCko"
    access_token="314737141-NRyP3oB7jFHXFpmmNroo5u6yPL7Njyj6WovwmMD8"
    access_token_secret="wIIn0RR5DhaqVgms5pm7w5v4G70zIlsAJpjXMt1zTc0ox"
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = API(auth)
    return api
def clean_tweet(tweet):
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
 
def get_tweet_sentiment(self, tweet):
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    # create TextBlob object of passed tweet text
    analysis = TextBlob(self.clean_tweet(tweet))
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'
if __name__ == "__main__":
    # calling main function
    main()
    