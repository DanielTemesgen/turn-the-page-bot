# [@turnthepagebot](http://twitter.com/turnthepagebot)

A twitter bot, written in python, that tweets the lyrics to The Streets - Turn the Page every 3 hours, forever.

It also updates the user description after every loop with the number of times the whole song has been tweeted.

## How?
1. Created a new account for the bot [here](twitter.com/turnthepagebot).
2. Registered for a Twitter Developer account.
3. Wrote the code on my local machine.
4. Pushed to GitHub.
5. Made a Heroku account.
6. Created a Heroku application.
7. Deployed the app via GitHub repo master branch.

## Why?
good question...

I wanted to complete a simple project to learn about the Twitter API and Heroku deployment via GitHub. Also ended up
learning about Heroku dyno cycling, which is why the code is more persistent now.

## What?
* `turn_the_page_bot/turn_the_page.py` - this is the class that breaks up the lyrics into tweets, tweets them
  out via Tweepy (a python wrapper for the Twitter API), it also updates the description after every loop.
* `turn_the_page_bot/twitter_client.py` - this acts as a gateway for all operations involving the Twitter API.
* `resources/lyrics.txt` - this file has the lyrics that will be tweeted.
* `main.py` - this acts as the entrypoint and is what Heroku runs.
