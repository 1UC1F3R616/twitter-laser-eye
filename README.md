# Twitter Last Seen Activity
Let your friends know when you are online and offline
- Laser-light eyes when online
- Last seen is mentioned in user bio


<p align="center">
<img src="https://pbs.twimg.com/media/ExLWFfpVcAcj6c6?format=jpg&name=900x900" width=900 height=250>
</p>
<p align="center">
<img src="https://pbs.twimg.com/media/ExLWFfsUUAQVscX?format=jpg&name=900x900" width=900 height=250>
</p>

## Setup
- Fork this repo and replace online.jpg and offline.jpg with your own images. To get laser-eyes use [this](https://memed.io/laser-eyes-meme-maker)
- Now before you proceed further update readme by changing the link of deploy button from `https://github.com/1UC1F3R616/twitter-laser-eye/tree/master` to something like `https://github.com/nightlyhacker/twitter-laser-eye/tree/master` where nightlyhacker has to be replaced with your GitHub username.
- Replace your bio [here](https://github.com/1UC1F3R616/twitter-laser-eye/blob/master/app.py) or comment out bio/description update code which is `api.update_profile(description=description)`
- Get `consumer_key`, `consumer_secret`, `access_token`, `access_token_secret` by creating your Twitter App from [here](https://developer.twitter.com/en/portal/apps/new)
- (You must update this link here before you click or else my image will be used) Click [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/1UC1F3R616/twitter-laser-eye/tree/master)
- Choose a random unpredictable App-Name and click 'Deploy app'
- Click 'manage app' and in settings click 'Reveal Config Vars'. Here add above 4 secrets with key-name as provided here and value is unique to every app.
- Click 'More' and hit 'Restart all dynos'
- Now you can visit your created web-app which is your controller, if you are getting 500 for some reason then check if all steps are done rightly or create an issue with proper error screenshot of logs which you can find inside 'More' --> 'View logs'

## Help
- [YT Video on how to setup]()
- [YT Video on Sample Usage]()

### Note
- Change your timezone because default is set to Asia/Kolkata. [Here](https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568) is a complete list.
---------------------------------------------------------------------------------------

<details close>
<summary>More Screenshots</summary>
<br>

![IMG_1495](https://user-images.githubusercontent.com/41824020/112268930-b804ab80-8c9d-11eb-8ee7-b2cbc8e50e43.jpg)

</details>
