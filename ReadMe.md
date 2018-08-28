# [@turnthepagebot](twitter.com/turnthepagebot)

A twitter bot, written in python, that tweets the lyrics to The Streets - Turn the Page every 3 hours, forever.

It also updates the user description after every loop with the number of times the whole song has been tweeted.

## How
1. Created a new account for the bot [here](twitter.com/turnthepagebot).
2. Registered for a Twitter Developer account.
3. Wrote the code on my local machine.
4. Pushed to GitHub.
5. Made a Heroku account.
6. Created a Heroku application.
7. Deployed the app via GitHub repo master branch.

## Why
good question...

I wanted to complete a simple project to learn about the Twitter API, Heroku deployment via GitHub.
Also ended up learning about Heroku dyno cycling, which is why the code is more persistent now.

## What
* lyrics.txt - this file has the lyrics that will be tweeted out
* turn_the_page.py - this is the python script that breaks up the lyrics into tweets, tweets them out via Tweepy - a python wrapper for the Twitter API, it also updates the description after every loop
* Procfile - this tells Heroku what to do upon starting the app, in this case I'd like it to run turn_the_page.py
* Pipfile + Pipfile.lock - files which tell Heroku this a Python app + what packages are required