import tweepy
import pandas as pd
import glob
from tweepy import TweepError


auth = tweepy.OAuthHandler("Jxxxxxxxxxxxxxxxxxxxq", "vdxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxL")
auth.set_access_token("5xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxk", "qxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxm")
api = tweepy.API(auth)


path = "twitter_hashtag_based_datasets/*.csv"
for fname in glob.glob(path):
    fname1= fname.split('/')[1]
    tweet_idf = pd.read_csv(fname, encoding = 'latin1', sep=',')
    tweet_idf["tweets"] = ""
    tweet_list=[]
    for i in tweet_idf['tweet_id']:
        try:
            tweet = api.get_status(i)
        except TweepError:
            continue
        tweet_list.append(tweet.text)
        i +=1
    tweet_idf['tweets'] = tweet_list
    export_csv_file1 = tweet_idf['tweets'].to_csv('Twitter_HB_datasets/' + fname1)
