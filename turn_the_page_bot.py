import time
import tweepy
from os import environ

#For Heroku to pick up the twitter api credentials they must be in this form, with the secrets being inputted into Heroku Dashboard
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = environ['ACCESS_TOKEN_SECRET']

#authenticates with twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#define functions
def get_linenumber():
	user = api.get_user(1025844712794718209)
	linenumber = int(user.description.split()[0]) #extracts line number from user description, always at index 0
	return linenumber
def increment_linenumber():
	user = api.get_user(1025844712794718209)
	linenumber, rest_of_description = user.description.split(' ', 1)
	new_linenumber = str(int(linenumber) + 1)
	if new_linenumber == '1':
		new_description = ' '.join([new_linenumber, 'line', user.description.split(' ', 2)[2]])
	elif new_linenumber == '2':
		new_description = ' '.join([new_linenumber, 'lines', user.description.split(' ', 2)[2]])
	else:
		new_description = ' '.join([new_linenumber, rest_of_description])
	api.update_profile(description = new_description)
def turn_the_page(current_description):
	''' Turns the page, e.g. '52 lines read. 2 pages turned' becomes '0 lines read. 3 pages turned.' '''
	split_desc = current_description.split() #splits description to list of words for easier access
	current_page = split_desc[3] #extracts the current page number from the user description, which is always at index 3
	new_page = str(int(current_page) + 1) #converts this to an integer, adds one then converts back to a string
	split_desc[3] = new_page #updates list with new page number
	split_desc[0] = '0' #this resets the line number back to 0
	new_description =  ' '.join(split_desc) #joins list of strings to one string with spaces
	return new_description

#open lyrics file
file = open("lyrics.txt") #opens lyrics.txt file
lyrics = file.readlines() #changes text file to a list of strings, with each element being a line in the lyrics.txt file

while True: #this while loop will run indefinitely
	api.update_status(lyrics[get_linenumber()]) #tweets the line
	increment_linenumber() #adds one to the number of lines, so the next line is tweeted later
	time.sleep(3*60*60) #the gap between tweets (in seconds)

	#this only runs when the last line has been tweeted
	if get_linenumber() == len(lyrics):
		#gets a twitter account User model' which is Python Class of all information asssociated with a user, in this case the bot
		user = api.get_user(1025844712794718209)
		new_description = turn_the_page(user.description)
		api.update_profile(description = new_description)