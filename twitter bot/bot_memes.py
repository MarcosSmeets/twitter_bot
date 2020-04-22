import tweepy as tp
import time
import os

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir('memes')
for model_image in os.listdir('.'):
    api.updade_with_media(model_image)
    time.sleep(3)