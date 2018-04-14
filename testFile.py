# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 18:03:35 2018

@author: niles
"""
import csv
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import json 
import pandas as pd
class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key="3YrMe9Y6q6jCUcTmvWnVZzjS2"
        consumer_secret="Y3fqkyAR2ZRw6Kin4vnzVd2QOnMC1DwLnWks3huO8wPpDHSCko"
        access_token="314737141-NRyP3oB7jFHXFpmmNroo5u6yPL7Njyj6WovwmMD8"
        access_token_secret="wIIn0RR5DhaqVgms5pm7w5v4G70zIlsAJpjXMt1zTc0ox"
        
        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")
 
    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        #return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
        return ' '.join(re.sub("#(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet).split())
        #return ' '.join(re.sub("https?:.*(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "URL", tweet).split())
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
    def writeCategory(self,keyWords,tweets):
        positiveTweets=[]
        negativeTweets=[]
        neutralTweets=[]
        
        with open('CategoricalData.csv', 'a',newline='') as myFile:
                writer = csv.writer(myFile)
                writer.writerow(["Tweets", "Sentiments"])
                writeCSVTwitterData=[]
                for word in keyWords:
                    for key,value in tweets.items():
                        if 'positive' in value:
                            if word in key:
                                positiveTweets.append(value)
                                writeCSVTwitterData.append(key)
                                writeCSVTwitterData.append(value)
                        elif 'negative' in value:
                            if word in key:
                                negativeTweets.append(value)
                                writeCSVTwitterData.append(key)
                                writeCSVTwitterData.append(value)
                        else:
                            if word in key:
                                neutralTweets.append(value)
                                writeCSVTwitterData.append(key)
                                writeCSVTwitterData.append(value)
                
                writer.writerow(writeCSVTwitterData)
                writeCSVTwitterData=[]
                
    def genCategories(self,tweets):
        categories=[]
        positiveEnvironment = ['environment','water','package','facility','reduce','energy','emission','population','clean','prevention','recycle','tobacco','fuel','climate','carbon']
        categories.append(positiveEnvironment)
        negativeEnvironment = ['hazardous','waste','agriculture','chemical','deplete']
        categories.append(negativeEnvironment)
        positiveCommunity = ['suppliers','local','education','woman','community','foundation','program','support','donation','giving','charitable','household','volunteer']
        categories.append(positiveCommunity)
        negativeCommunity = ['dispute']
        categories.append(negativeCommunity)
        positiveHumanCapital = ['employee','right','diversity','workplace','human','human right','workforce','aids','union','sharing','retirement benefits','freedom']
        categories.append(positiveHumanCapital)
        negativeHumanCapital = ['layoff', 'reductions']
        categories.append(negativeHumanCapital)
        positiveDiversity = ['diversity','work-life','women','minority','disability','director','gay','lesbian']
        categories.append(positiveDiversity)
        positiveProduct = ['innovation','safety','product','customer','demand','technology']
        categories.append(positiveProduct)
        negativeProduct = ['antitrust']
        categories.append(negativeProduct)
        positiveGovernance = ['code','policy','board','compliance','director','corporate','committee','transparency','accountability']
        categories.append(positiveGovernance)
        
        for p in range(len(categories)):
            self.writeCategory(categories[p],tweets)
    
    def categorizeTweets(self,tweets):
        categorizedTweets=[]
        with open('OutputSentiments.csv', 'a',newline='',encoding="utf-8") as outFile:
            writer = csv.writer(outFile)
            with open('keyWordsList.json', 'r') as keyWordsFile:
                for line in keyWordsFile:
                    keyWords=json.loads(line)
                    for category in keyWords:
                        for categ,categValues in category.items():
                            writer.writerow([categ, "Sentiments"])
                            for keyWord in categValues:
                                for tweet in tweets:
                                    if keyWord in tweet:
                                        categorizedTweets.append(tweet)
                                        
                                        writeCSVTwitterData=[]
                                        writeCSVTwitterData.append(self.clean_tweet(tweet))                        
                                        writeCSVTwitterData.append(self.get_tweet_sentiment(tweet))
                                        writer.writerow(writeCSVTwitterData)                                                                
                                                            
            
    def categorizeTweetsKeywords(self,tweets):
        categorizedTweets=[]
        environmentTweets=[]
        environmentSentiments=[]
        communityTweets=[]
        communitySentiments=[]
        human_capitalTweets=[]
        human_capitalSentiments=[]
        diversityTweets=[]
        diversitySentiments=[]
        productTweets=[]
        productSentiments=[]
        governanceTweets=[]
        governanceSentiments=[]
        with open('keyWordsList.json', 'r') as keyWordsFile:                
                       for line in keyWordsFile:
                           keyWords=json.loads(line)
                           for category in keyWords:
                               for categ,categValues in category.items():
                                   for keyWord in categValues:
                                       for tweet in tweets:
                                           if keyWord in tweet:
                                               categorizedTweets.append(self.clean_tweet(tweet))                                               
                                               if categ =='Environment':                                                   
                                                   environmentTweets.append(self.clean_tweet(tweet))
                                                   environmentSentiments.append(self.get_tweet_sentiment(tweet))
                                               elif categ =='Community':
                                                   communityTweets.append(self.clean_tweet(tweet))
                                                   communitySentiments.append(self.get_tweet_sentiment(tweet))
                                               elif categ =='Human capital':
                                                   human_capitalTweets.append(self.clean_tweet(tweet))
                                                   human_capitalSentiments.append(self.get_tweet_sentiment(tweet))
                                               elif categ =='Diversity':
                                                   diversityTweets.append(self.clean_tweet(tweet))
                                                   diversitySentiments.append(self.get_tweet_sentiment(tweet))
                                               elif categ =='Product':
                                                   productTweets.append(self.clean_tweet(tweet))
                                                   productSentiments.append(self.get_tweet_sentiment(tweet))
                                               elif categ =='Governance':
                                                   governanceTweets.append(self.clean_tweet(tweet))
                                                   governanceSentiments.append(self.get_tweet_sentiment(tweet))
        
        df1 = pd.DataFrame({'Environmental Tweets': environmentTweets,'Sentiments': environmentSentiments})
        df2 = pd.DataFrame({'Community Tweets': communityTweets,'Sentiments': communitySentiments})
        df3 = pd.DataFrame({'Human Capital Tweets': human_capitalTweets,'Sentiments': human_capitalSentiments})
        df4 = pd.DataFrame({'Diversity Tweets': diversityTweets,'Sentiments': diversitySentiments})
        df5 = pd.DataFrame({'Product Tweets': productTweets,'Sentiments': productSentiments})
        df6 = pd.DataFrame({'Governance Tweets': governanceTweets,'Sentiments': governanceSentiments})
        writer = pd.ExcelWriter('Categorized_Tweets.xlsx', engine='xlsxwriter')
        df1.to_excel(writer, sheet_name='Environment')
        df2.to_excel(writer, sheet_name='Community')
        df3.to_excel(writer, sheet_name='Human Capital')
        df4.to_excel(writer, sheet_name='Diversity')
        df5.to_excel(writer, sheet_name='Product')
        df6.to_excel(writer, sheet_name='Governance')
        writer.save()        
        #print(categorizedTweets)                           
        try:
            with open('tweetSentiments.csv', 'a',newline='',encoding="utf-8") as myFile:
                writer = csv.writer(myFile)
                writer.writerow(["Tweets", "Sentiments"])
                for tweet in categorizedTweets:
                    parsed_tweet = {}
                    writeCSVTwitterData=[]
                    parsed_tweet['text'] = self.clean_tweet(tweet)
                    writeCSVTwitterData.append(parsed_tweet['text'])                        
                    parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet)
                    writeCSVTwitterData.append(parsed_tweet['sentiment'])
                    writer.writerow(writeCSVTwitterData)                                                                
            
        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))
        return 0                   
    def get_tweets(self):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []
        retweets=[]
        try:
            with open('tweetsNewAgain.json', 'r') as f:                
                for line in f:
                    if len(line) > 1:                                
                        tweetLine = json.loads(line)      
                        for tweetText in tweetLine:
                            #tweetList=[d['text'] for d in tweet if 'text' in d]    
                            #print(tweetText)
                            if int(tweetText['retweets']) > 0:
                                if tweetText['text'] not in tweets:
                                    tweets.append(tweetText['text'])
                                else:
                                    retweets.append(tweetText['text'])                                                      
                            else:
                                tweets.append(tweetText['text'])                     
                    else:
                        break
                self.categorizeTweetsKeywords(tweets)
                #self.categorizeTweets(tweets)                                    
                #self.genCategories(tweets)
                return tweets
        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))
 
def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets()
 
    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    # percentage of neutral tweets
    #print("Neutral tweets percentage: {} % \".format(100*len(tweets - ntweets - ptweets)/len(tweets)))
 
    # printing first 5 positive tweets
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
        print(tweet['text'])
 
    # printing first 5 negative tweets
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])
 
if __name__ == "__main__":
    # calling main function
    main()
