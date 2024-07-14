from ntscraper import Nitter
from pprint import pprint
import ast

LOAD_DATA = False
# since -> start date
# until -> last date

if LOAD_DATA:
    scraper = Nitter(log_level=1, skip_instance_check=False)
    tweets = scraper.get_tweets("akshitkhatri20", mode="user", number=5)
    pprint(tweets)
    with open("tweets.txt", 'w', encoding='utf-8') as tweet:
        tweet.write(str(tweets))
    LOAD_DATA = False
else:
    with open("tweets.txt", encoding='utf-8') as tweet:
        tweets = tweet.read()
        tweets = ast.literal_eval(tweets)

#pprint(tweets)
tweets_csv = []
for tweet in tweets['tweets']:
    tweet_csv = {
        'link': [],
        'text': [],
        'user': [],
        'quotes': [],
        'retweets': [],
        'comments': []
    }
    tweet_csv['link'].append(tweet['link'])
    tweet_csv['text'].append(tweet['text'])
    tweet_csv['user'].append(tweet['user']['name'])
    tweet_csv['quotes'].append(tweet['stats']['quotes'])
    tweet_csv['retweets'].append(tweet['stats']['retweets'])
    tweet_csv['comments'].append(tweet['stats']['comments'])
    tweets_csv.append(tweet_csv)

pprint(tweets_csv)
