from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import API
consumer_key="3YrMe9Y6q6jCUcTmvWnVZzjS2"
consumer_secret="Y3fqkyAR2ZRw6Kin4vnzVd2QOnMC1DwLnWks3huO8wPpDHSCko"

access_token="314737141-NRyP3oB7jFHXFpmmNroo5u6yPL7Njyj6WovwmMD8"
access_token_secret="wIIn0RR5DhaqVgms5pm7w5v4G70zIlsAJpjXMt1zTc0ox"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

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