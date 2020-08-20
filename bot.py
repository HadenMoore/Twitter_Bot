import tweepy
#import Tkinter
import config 

# Authorization 
auth = tweepy.OAuthHandler(consumer_Key, consumer_Secret)
auth.set_access_Token(access_Token, access_Token_secret)

api = tweepy.API(auth) 

# Quick Check 
user = api.me()
print(user.name)