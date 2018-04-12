# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 02:19:04 2018

@author: niles
"""
from tweepy import OAuthHandler 
from tweepy import API 
import sys
# Consumer keys and access tokens, used for OAuth
                            
def get_twitter_auth():
    try:
        consumer_key = '3YrMe9Y6q6jCUcTmvWnVZzjS2'
        consumer_secret = 'Y3fqkyAR2ZRw6Kin4vnzVd2QOnMC1DwLnWks3huO8wPpDHSCko'
        access_token = '314737141-NRyP3oB7jFHXFpmmNroo5u6yPL7Njyj6WovwmMD8'
        access_token_secret = 'wIIn0RR5DhaqVgms5pm7w5v4G70zIlsAJpjXMt1zTc0ox'
    except:
        sys.stderr.write("Authentication Issue")
        sys.exit(0)
    # OAuth process, using the keys and tokens
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth
def get_twitter_client():
    # Creation of the actual interface, using authentication
    api = get_twitter_auth()
    client = API(api)
    return client
 
# Sample method, used to update a status
#api.update_status('Hello Python Central!')

#My information
#user = api.me() 
#print('Name: ' + user.name)
#print('Location: ' + user.location)
#print('Friends: ' + str(user.friends_count))
 
