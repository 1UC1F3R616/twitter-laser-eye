import os

from flask import Flask, request
from flask import render_template

app = Flask(__name__)

import tweepy
from datetime import datetime

# assign the values accordingly
consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
            if request.form.get('ONLINE') == 'ONLINE':
                # authorization of consumer key and consumer secret
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                
                # set access to user's access key and access secret 
                auth.set_access_token(access_token, access_token_secret)
                
                # calling the api 
                api = tweepy.API(auth)
                
                # the file path
                filename = "online.jpg"
                
                # updating the profile picture
                api.update_profile_image(filename)
                description = "this too shall pass. Online"
                api.update_profile(description=description)
                print("ONLINE")

            elif  request.form.get('OFFLINE') == 'OFFLINE':
                # authorization of consumer key and consumer secret
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                
                # set access to user's access key and access secret 
                auth.set_access_token(access_token, access_token_secret)
                
                # calling the api 
                api = tweepy.API(auth)
                
                # the file path
                filename = "offline.jpg"
                
                # updating the profile picture
                api.update_profile_image(filename)
                description = "this too shall pass. Last-Online: {}".format(datetime.now().strftime("%d-%m-%y %H:%M:%S"))
                api.update_profile(description=description)
                print("OFFLINE")
            else:
                # pass # unknown
                return render_template("index.html")

    elif request.method == 'GET':
        print("No Post Back Call")
    return render_template("index.html")

if __name__ == '__main__':
    app.run() # when running on heroku