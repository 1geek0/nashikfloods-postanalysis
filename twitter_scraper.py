import sys

import pandas as pd
import tweepy

ckey = 'MA9feEpiqBT1vVtuOFuOVBqIy'
csecret = '3KoiiECHtxz404WwoRYHl5V6WxARpxkZgd0CTIBEnW5Pfkztkd'
atoken = '760746093667692544-AkktH6WZhLz0KONkU0PVmBszQlXawuU'
asecret = 'FU9vNQ8FpxipPmJxeuQZ8gEMrkwhFFWuJAnmLRVMxz3xK'


def toDataFrame(tweets):
    # COnvert to data frame
    DataSet = pd.DataFrame()

    DataSet['tweetID'] = [tweet.id for tweet in tweets]
    DataSet['tweetText'] = [tweet.text.encode('utf-8') for tweet in tweets]
    DataSet['tweetRetweetCt'] = [tweet.retweet_count for tweet in tweets]
    DataSet['tweetFavoriteCt'] = [tweet.favorite_count for tweet in tweets]
    DataSet['tweetSource'] = [tweet.source for tweet in tweets]
    DataSet['tweetCreated'] = [tweet.created_at for tweet in tweets]
    DataSet['userID'] = [tweet.user.id for tweet in tweets]
    DataSet['userScreen'] = [tweet.user.screen_name for tweet in tweets]
    DataSet['userName'] = [tweet.user.name for tweet in tweets]
    DataSet['userCreateDt'] = [tweet.user.created_at for tweet in tweets]
    DataSet['userDesc'] = [tweet.user.description for tweet in tweets]
    DataSet['userFollowerCt'] = [tweet.user.followers_count for tweet in tweets]
    DataSet['userFriendsCt'] = [tweet.user.friends_count for tweet in tweets]
    DataSet['userLocation'] = [tweet.user.location for tweet in tweets]
    DataSet['userTimezone'] = [tweet.user.time_zone for tweet in tweets]
    DataSet['Coordinates'] = [tweet.coordinates for tweet in tweets]
    DataSet['GeoEnabled'] = [tweet.user.geo_enabled for tweet in tweets]
    DataSet['Language'] = [tweet.user.lang for tweet in tweets]
    tweets_place = []
    # users_retweeted = []
    for tweet in tweets:
        if tweet.place:
            tweets_place.append(tweet.place.full_name)
        else:
            tweets_place.append('null')
    DataSet['TweetPlace'] = [i for i in tweets_place]
    # DataSet['UserWhoRetweeted'] = [i for i in users_retweeted]

    return DataSet


OAUTH_KEYS = {'consumer_key': ckey, 'consumer_secret': csecret, 'access_token_key': atoken,
              'access_token_secret': asecret}
# auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
auth = tweepy.AppAuthHandler('1wnO9ke6fgV2jMrmmQhZ2vTTU', 'I3Ev8FixRZ2XLic4ZwmydWpgPMSIVtDrmCKGmKUIuKX90bI8Br')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
if not api:
    print("Can't Authenticate")
    sys.exit(-1)
else:
    print(" Scraping data now")  # Enter lat and long and radius in Kms
    cursor = tweepy.Cursor(api.search,
                           q='Nashik',
                           since='2016-08-01',
                           until='2016-08-04',
                           count=5000,
                           include_rts=False,
                           exclude_replies=False)
    results = []
    print("Tweets: " + str(cursor.items().num_tweets))
    x = 0
    for item in cursor.items(5000):  # Remove the limit to 1000
        x += 1
        print(x)
        if not item.retweet:
            print("Found One")
            results.append(item)
    DataSet = toDataFrame(results)
    DataSet.to_csv('data.csv', index=False)
