import tweepy
from tweepy import *
import pandas as pd
import csv
import re 
import string
import preprocessor as p
 
consumer_key = 'UqHRhFlJ7KXj5onzKFkdUI9uq'
consumer_secret = 'm7xO2XlzuyuQ7gQtvwKz4d7weZIl0Zs0KiRrakRjzCaQoUzkgK'
access_key = '1487411554215555072-6ou3xZf8SB3KIOYbzz4R1RjYiy73Z1'
access_secret = 'UibHIscgD3o8TRXJ8DfPUC3Yu02ENKkj5cSPKtbMXNOkc'

 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
 
api = tweepy.API(auth,wait_on_rate_limit=True)
 
csvFile = open('file-name', 'a')
csvWriter = csv.writer(csvFile)
 
search_words = "sex"      # enter your words
new_search = search_words + " -filter:retweets"
 
for tweet in tweepy.Cursor(api.search,q=new_search,count=100,
                           lang="en",
                           since_id=0).items():
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8')])