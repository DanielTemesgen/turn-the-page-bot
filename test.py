import time
import config #imports the config.py file to get the api credentials, which aren't exposed

file = open("lyrics.txt") #opens lyrics.txt file

lyrics = file.readlines() #changes text file to a list of strings, with each element being a line in the lyrics.txt file

linenumber = 0 # initialises the linenumber as 0 before the while loop

while True: #this while loop will run indefinitely
	print(lyrics[line number]) #tweets the line
	linenumber += 1 #adds one to the number of lines, so the next line is tweeted
	time.sleep(5) #the gap between tweets (in seconds)

	#this only runs when the last line has been tweeted
	if linenumber == len(lyrics):
		linenumber = 0 #resets the line number back to 0

		#ADD THE BIO UPDATE HERE
		#READS THE BIO OF THE TWITTER BOT, e.g. '3 pages turned'
		#Extracts the first number i.e. 3
		# Makes new string with the number increased by 1 i.e 4 pages turned
		# Assigns this new string to the description only if it's less than 160 characters


