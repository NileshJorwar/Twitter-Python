# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 03:19:27 2018

@author: niles
"""

import re
from textblob import TextBlob

# =============================================================================
# import json
# import nltk
# nltk.download('punkt')
# from nltk.tokenize import word_tokenize 
# with open('python.json', 'r') as f:
#     line = f.readline() # read only the first tweet/line
#     tweet = json.loads(line) # load it as Python dict
#     print(json.dumps(tweet, indent=4)) # pretty-print
# 
# tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
# print(word_tokenize(tweet))
# =============================================================================


 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

# =============================================================================
# with open('python.json', 'r') as f:
#     for line in f:
#         tweet = json.loads(line)
#         tokens = preprocess(tweet['text'])
#         print(json.dumps(tweet, indent=4))
#         #do_something_else(tokens)
# #tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
# =============================================================================
#print(preprocess(tweet))
# ['RT', '@marcobonzanini', ':', 'just', 'an', 'example', '!', ':D', 'http://example.com', '#NLP']

def clean_tweet(self, tweet):
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