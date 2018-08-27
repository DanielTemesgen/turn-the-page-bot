import time
import tweepy
import config #imports the config.py file to get the api credentials, which aren't exposed.

#authenticates with twitter
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
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

linenumber = 0 # initialises the linenumber as 0 before the while loop

while True: #this while loop will run indefinitely
	api.update_status(lyrics[linenumber]) #tweets the line
	linenumber += 1 #adds one to the number of lines, so the next line is tweeted
	time.sleep(60*60*3) #the gap between tweets (in seconds)

	#this only runs when the last line has been tweeted
	if linenumber == len(lyrics):
		#gets a twitter 'user model' which is Python Class of all information asssociated with a user, in this case the bot
		user = api.get_user(1025844712794718209)
		new_description = turn_the_page(user.description)
		api.update_profile(description = new_description)
		linenumber = 0 #resets the line number back to 0

		#ADD THE BIO UPDATE HERE
		#READS THE BIO OF THE TWITTER BOT, e.g. '3 pages turned'
		#Extracts the first number i.e. 3
		# Makes new string with the number increased by 1 i.e 4 pages turned
		# Assigns this new string to the description only if it's less than 160 characters


