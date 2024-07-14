import tweepy
from oauthlib.uri_validate import query
from tweepy import OAuthHandler

api_key = 'JywEKy6S0hesw0n8HgqP4rRSW'
api_secret = 'IW875CShj1fRhkjUCsX9FppIX4O8nraUVrwDLFvSvzlAvBiu12'
access_token = '1756290151007842304-f3FTPnSmdrph9oM1e9MYvh3Yt4eJH6'
access_secret = 'jQJQduLEWMLjQAWh8hI15wSFJQWzfcMBX56RPVumEDm8F'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAADQtuwEAAAAAJP4icUNrHDbclatc%2B2BEVBWqchY%3DLnS36bRiSjjG8d7d2bLsY6jW8x1fWcSQk9uD5WWF7bKAGTZaTI'

#client = tweepy.Client(bearer_token=bearer_token)
#user = client.get_me()
#user_data = user.data
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)
user = api.verify_credentials()
user = api.get_user(screen_name=user.screen_name)
print(f"User ID: {user.id}")
print(f"Username: {user.screen_name}")
print(f"Name: {user.name}")
#response = client.get_me()
#auth = tweepy.OAuthHandler(api_key, api_secret)
#auth.set_access_token(access_token, access_secret)

#api = tweepy.API(auth)
#user = api.verify_credentials()
#user = api.get_user(screen_name=user.screen_name)

print(f"User ID: {user_data.id}")
print(f"Username: {user_data.username}")
print(f"Name: {user_data.name}")
#auth = OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_secret)

#api = tweepy.API(auth, wait_on_rate_limit=True)

#for status in tweepy.Cursor(api.get_me, q=query, lang="en", tweet_mode='extended').items():
#    print(status.text)
