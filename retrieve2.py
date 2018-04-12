# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 12:20:31 2018

@author: niles
"""
from tweepy import Stream
from tweepy.streaming import StreamListener
import tweepy
consumer_key="3YrMe9Y6q6jCUcTmvWnVZzjS2"
consumer_secret="Y3fqkyAR2ZRw6Kin4vnzVd2QOnMC1DwLnWks3huO8wPpDHSCko"

access_token="314737141-NRyP3oB7jFHXFpmmNroo5u6yPL7Njyj6WovwmMD8"
access_token_secret="wIIn0RR5DhaqVgms5pm7w5v4G70zIlsAJpjXMt1zTc0ox"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#publicTweets = api.home_timeline()
#print(publicTweets)
#for t in publicTweets:
#    print(t)
users = api.get_user('twitter')
#print(users)
print(users.screen_name)
print(users.followers_count)
#for friends in users.friends():
#    print(friends.screen_name)
#for friend in tweepy.cursor(api.followers).items():
#    print(friend)
#
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
twitter_stream.filter(track=['#ABBOTT LABORATORIES'])

with open('python.json', 'w') as f:
    for t in tweepy.Cursor(api.search,q="obama",since="2006-04-03",until = "2017-04-03",lang="en").items(10):
        #f.write(jsonpickle.encode(t._json, unpicklable=False) + '\n')
        print(t.text.encode("utf-8")) 
        #f.write(str(t.text.encode("utf-8")))
        
