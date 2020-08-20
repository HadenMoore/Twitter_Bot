import tweepy
#import Tkinter
import config 

# Authorization 
auth = tweepy.OAuthHandler(config.consumer_Key, config.consumer_Secret)
auth.set_access_Token(config.access_Token, config.access_Token_secret)

api = tweepy.API(auth) 

# Quick Check 
user = api.me()
print(user.name)