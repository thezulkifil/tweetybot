import os as _os
import secrets
import dotenv as _dotenv
import time as _time
import tweepy as _tweepy
import services as _services
from services import get_tweet
import unsplash as _unsplash

_dotenv.load_dotenv()

API_KEY = _os.environ["TWITTER_API_KEY"]
SECRET_KEY = _os.environ["TWITTER_API_SECRET_KEY"]
ACCESS_TOKEN = _os.environ["TWITTER_ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = _os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

def _get_twtter_api():
    auth = _tweepy.OAuthHandler(API_KEY, SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    twitter_api = _tweepy.API(
        auth, wait_on_rate_limit=True
    )


    return twitter_api
    
def _write_tweet():
    tweet = _services.get_tweet()
    twitter_api = _get_twtter_api()
    twitter_api.update_status(tweet)


def run():
    while True:
        _write_tweet()
        _time.sleep(1300)

if __name__ == "__main__":
    run()