import os
import sys
from tweepy import API
from tweepy import OAuthHandler

consumer_key = "UAS7zJt23fOj4cPoiWFytb0pt"
consumer_secret = "yKMr5dtIvG8OY0dFVGCDvIHf44IxGBkKvsHZhN0ivDJx95VfY1"
access_token = "547035595-bBPOPUdPa6tBU0XrRJSCWusZTT3mnvaPzcSPjKWQ"
access_token_secret = "E8aocBO3lFTMpPY3LDRmdlyDMmL0R8ydNfg23Iio6nnBR"

def get_twitter_auth():
consumer_key = "UAS7zJt23fOj4cPoiWFytb0pt"
consumer_secret = "yKMr5dtIvG8OY0dFVGCDvIHf44IxGBkKvsHZhN0ivDJx95VfY1"
access_token = "547035595-bBPOPUdPa6tBU0XrRJSCWusZTT3mnvaPzcSPjKWQ"
access_token_secret = "E8aocBO3lFTMpPY3LDRmdlyDMmL0R8ydNfg23Iio6nnBR"
    
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

def get_twitter_client():
    auth = get_twitter_auth()
    client = API(auth)
    return(client)
    