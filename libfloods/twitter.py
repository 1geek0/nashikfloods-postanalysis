import tweepy
import os

ckey = 'MA9feEpiqBT1vVtuOFuOVBqIy'
csecret = '3KoiiECHtxz404WwoRYHl5V6WxARpxkZgd0CTIBEnW5Pfkztkd'
atoken = '760746093667692544-AkktH6WZhLz0KONkU0PVmBszQlXawuU'
asecret = 'FU9vNQ8FpxipPmJxeuQZ8gEMrkwhFFWuJAnmLRVMxz3xK'

OAUTH_KEYS = {'consumer_key': ckey, 'consumer_secret': csecret, 'access_token_key': atoken,
              'access_token_secret': asecret}
auth = tweepy.OAuthHandler("MA9feEpiqBT1vVtuOFuOVBqIy", "3KoiiECHtxz404WwoRYHl5V6WxARpxkZgd0CTIBEnW5Pfkztkd")
auth.set_access_token(atoken, asecret)
#auth = tweepy.AppAuthHandler('1wnO9ke6fgV2jMrmmQhZ2vTTU', 'I3Ev8FixRZ2XLic4ZwmydWpgPMSIVtDrmCKGmKUIuKX90bI8Br')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def tweetPhoto(location, photoPath):
    home = os.path.expanduser("~")
    photoPath = home + photoPath
    tweetString = location
    print("Tweet" + photoPath)
    file1 = open(photoPath)
    api.update_with_media(photoPath, status=tweetString)
    pass
