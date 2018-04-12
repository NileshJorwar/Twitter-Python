# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 02:39:31 2018

@author: niles
"""

from tweepy import Cursor
from intro_twitter import get_twitter_client

def process_or_store(tweet):
    print(tweet)    

if __name__ == "__main__":
    client = get_twitter_client()
    for status in Cursor(client.home_timeline).items(10):
        print(status.text)
    for status in Cursor(client.home_timeline).items(10):
        # Process a single status
        process_or_store(status._json)
