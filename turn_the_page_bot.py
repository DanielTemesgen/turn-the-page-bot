import time
import tweepy
from os import environ

#For Heroku to pick up the twitter api credentials they must be in this form, with the secrets being inputting into Heroku Dashboard
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = environ['ACCESS_TOKEN_SECRET']

#authenticates with twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def turn_the_page(current_description): 
	''' Adds 1  to the current description, e.g. '62 pages turned.' becomes '63 pages turned.' '''
	current_page = current_description.split()[0] #extracts the number from the user description, which is always the first 'word'
	new_page = str(int(current_page) + 1) #converts this to an integer, adds one then converts back to a string
	constant = current_description.split()[1:] #initalises the constant i.e. the rest of the original description
	constant.insert(0, new_page) #inserts the new page number into the constant, now we have a the new description but in list form
	separator = ' ' #need to define a separator for the .join() method below
	new_description = separator.join(constant) #this method converts a list of strings to one string, separated by a space i.e.' ' 
	return new_description #the function returns this new description

file = open("lyrics.txt") #opens lyrics.txt file
lyrics = file.readlines() #changes text file to a list of strings, with each element being a line in the lyrics.txt file

linenumber = 0 # initialises the linenumber as 0 before the while loop, if I'm redeploying this I should change this to the line number of the most recent tweet

while True: #this while loop will run indefinitely
	api.update_status(lyrics[linenumber]) #tweets the line
	linenumber += 1 #adds one to the number of lines, so the next line is tweeted
	time.sleep(3*60*60) #the gap between tweets (in seconds)

	#this only runs when the last line has been tweeted
	if linenumber == len(lyrics):
		#gets a twitter 'user model' which is Python Class of all information asssociated with a user, in this case the bot
		user = api.get_user(1025844712794718209)
		new_description = turn_the_page(user.description)
		api.update_profile(description = new_description)
		linenumber = 0 #resets the line number back to 0