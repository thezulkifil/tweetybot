from typing import Dict, List
import json as _json
import random as _random

def _get_quotes() -> List:
    with open("quotes.json") as quotes_file:
        quotes = _json.load(quotes_file)

    return quotes

def _get_random_quote() -> Dict:
    quotes = _get_quotes()
    quote = _random.choice(quotes)

    return quote

def _form_tweet(quote: Dict[str, str]) -> str:
    author = quote["author"].strip(",")
    genre = quote["genre"]
    tweet = f"{quote['quote']} words: {author} #{genre}"

    return tweet

def _is_valid_character(tweet: str) -> bool:
    return len(tweet) <= 200

def get_tweet():
    while True:
        quote = _get_random_quote()
        tweet = _form_tweet(quote) 
        if _is_valid_character(tweet):
            return tweet
