# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 03:08:07 2018

@author: niles
"""

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener 
import json
consumer_key = '3YrMe9Y6q6jCUcTmvWnVZzjS2'
consumer_secret = 'Y3fqkyAR2ZRw6Kin4vnzVd2QOnMC1DwLnWks3huO8wPpDHSCko'
access_token = '314737141-NRyP3oB7jFHXFpmmNroo5u6yPL7Njyj6WovwmMD8'
access_token_secret = 'wIIn0RR5DhaqVgms5pm7w5v4G70zIlsAJpjXMt1zTc0ox' 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])

def process_or_store(tweet):
    print(json.dumps(tweet))

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    #process_or_store(status._json)    

