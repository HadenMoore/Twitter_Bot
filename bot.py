import tweepy
from tweepy.auth import OAuthHandler
import config 
import tkinter as tk
from tkinter import *


# Authorization 
auth = tweepy.OAuthHandler(config.consumer_Key, config.consumer_Secret)
auth.set_access_token(config.access_Token, config.access_Token_secret)

api = tweepy.API(auth) 

# Quick Check 
user = api.me()
print(user.name)
print(user.location)

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()

print('Followed Everyone that is Currently Following.' + user.name)

root = Tk()
# GUI Labels: 
label1 = Label(root, text = "Search")
E1 = Entry(root, bd = 5)

label2 = Label(root, text = "Number of Tweets")
E2 = Entry(root, bd = 5) 

label3 = Label(root, text = "Response")
E3 = Entry(root, bd = 5)

label4 = Label(root, text = "Care to Reply?")
E4 = Entry(root, bd = 5)

label5 = Label(root, text = "Care to Retweet?")
E5 = Entry(root, bd = 5)

label6 = Label(root, text = "Shall I Favorite this?")
E6 = Entry(root, bd = 5)

label7 = Label(root, text = "Shall I Follow Them?")
E7 = Entry(root, bd = 5)

def getE1(): 
    return E1.get()

def getE2():
    return E2.get()

def getE3():
    return E3.get()

def getE4():
    return E4.get()

def getE5():
    return E5.get()

def getE6():
    return E6.get()

def getE7():
    return E7.get()

def mainFunction(): 
    getE1()
    search = getE1()
    getE2()
    numberOfTweets = getE2()
    numberOfTweets = int(numberOfTweets)
    getE3()
    phrase = getE3()
    getE4()
    reply = getE4()
    getE5()
    retweet = getE5()
    getE6()
    favorite = getE6()
    getE7()
    follow = getE7()

    if reply == "Yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try: 
                # Reply
                print('\nTweet by: @' + tweet.user.screen_name)
                print('ID: @' +str(tweet.user.id))
                tweetId = tweet.user.id
                username = tweet.user.screen_name
                api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
                print("Replied with" + phrase)
            
            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break
    
    if favorite == "Yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try: 
                # Favorite
                tweet.favorite()
                print('I took the liberty of Favoriting The Tweet, Sir')
            except tweepy.TweepError as e: 
                print(e.reason)
            except StopIteration:
                break
    
    if follow == 'Yes': 
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try: 
                #Follow 
                tweet.user.follow()
                print('I took the liberty and Follow the User, sir.')
            except tweepy.TweepError as e: 
                print(e.reason)
            except StopIteration:
                break

submit = Button(root, text="Submit", command = mainFunction)

label1.pack()
E1.pack()
label2.pack()
E2.pack()
label3.pack()
E3.pack()
label4.pack()
E4.pack()
label5.pack()
E5.pack()
label6.pack()
E6.pack()
label7.pack()
E7.pack()
submit.pack(side=BOTTOM)

root.mainloop()