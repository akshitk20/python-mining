import tweepy
from tweepy import OAuthHandler

consumer_key = "JywEKy6S0hesw0n8HgqP4rRSW"
consumer_secret = "IW875CShj1fRhkjUCsX9FppIX4O8nraUVrwDLFvSvzlAvBiu12"
access_token = "1756290151007842304-f3FTPnSmdrph9oM1e9MYvh3Yt4eJH6"
access_secret = "jQJQduLEWMLjQAWh8hI15wSFJQWzfcMBX56RPVumEDm8F"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.get_friends).items():
    print(status.text)

