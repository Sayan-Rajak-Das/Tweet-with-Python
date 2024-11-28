import os
import tweepy
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve API credentials
API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Initialize the client with the Bearer Token
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

print("API_KEY:", API_KEY)
print("API_SECRET_KEY:", API_SECRET_KEY)
print("ACCESS_TOKEN:", ACCESS_TOKEN)
print("ACCESS_TOKEN_SECRET:", ACCESS_TOKEN_SECRET)
print("BEARER_TOKEN:", BEARER_TOKEN)

# Post a tweet
try:
    response = client.create_tweet(text="Hello, Twitter! This is my first tweet using OAuth 2.0 🚀")
    print("Tweet posted successfully!")
    print("Tweet ID:", response.data["id"])
except tweepy.TweepyException as e:
    print(f"Error posting tweet: {e}")
