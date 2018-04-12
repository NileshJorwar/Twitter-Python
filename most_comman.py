# coding: utf-8



# Imports you'll need.
from collections import Counter
import matplotlib.pyplot as plt
import networkx as nx
import sys
import time
from tweepy import OAuthHandler 
from tweepy import API 
from tweepy.cursor import Cursor
consumer_key = '3YrMe9Y6q6jCUcTmvWnVZzjS2'
consumer_secret = 'Y3fqkyAR2ZRw6Kin4vnzVd2QOnMC1DwLnWks3huO8wPpDHSCko'
access_token = '314737141-NRyP3oB7jFHXFpmmNroo5u6yPL7Njyj6WovwmMD8'
access_token_secret = 'wIIn0RR5DhaqVgms5pm7w5v4G70zIlsAJpjXMt1zTc0ox'


# This method is done for you.


def main():
    """ Main method. You should not modify this. """
    twitter = get_twitter()
    print('Connection Established')
    screen_names = read_screen_names('candidates.txt')
    print('Read screen names: %s' % screen_names)
    print('Established Twitter connection.')
    
    user = twitter.get_user(screen_names[0])
    print('USer %s'% user.screen_name)
    print ('Followers %d' % user.followers_count)
    for friend in user.friends():
        print (friend.screen_name)
    for friend in Cursor(twitter.friends).items():
        # Process the friend here
        print(friend)
    for status in Cursor(twitter.friends_timeline).items(200):
        print(status)
    for tweet in tweepy.Cursor(twitter.search,q=screen_names[0],since="2014-01-01",until="2014-02-01",lang="en").items():
        print(tweet)
    #print('Read screen names: %s' % screen_names)
    
def get_twitter():
    """ Construct an instance of TwitterAPI using the tokens you entered above.
    Returns:
      An instance of TwitterAPI.
    """
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    client = API(auth)
    return client


def read_screen_names(filename):
    """
    Read a text file containing Twitter screen_names, one per line.

    Params:
        filename....Name of the file to read.
    Returns:
        A list of strings, one per screen_name, in the order they are listed
        in the file.

    Here's a doctest to confirm your implementation is correct.
    >>> read_screen_names('candidates.txt')
    ['DrJillStein', 'GovGaryJohnson', 'HillaryClinton', 'realDonaldTrump']
    """
    ###TODO
    #pass
    file = open(filename, "r")
    names = []
    for line in file:
        names.append(line.strip())
    return names






if __name__ == '__main__':
    main()



# That's it for now! This should give you an introduction to some of the data we'll study in this course.
