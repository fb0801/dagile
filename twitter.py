'''cmd version of twitter bot
	
part of https://github.com/fb0801/dagile created by Farhan


'''

#modules for application
import time
#import dateandtime




# define the countdown func.
def countdown(t):
	
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1
	
	print('Fire in the hole!!')


def start():
	# input time in seconds
	t = input("Enter the time in seconds: ")

	# function call
	countdown(int(t))


def twitter():
	url ="https://twitter.com/home?lang=en"
	
def login():
	pass

def retweet():
	pass

def twitterFollow():
	pass

def TweetLike():
	pass

def files():
	pass

if __name__ == "__main__":
    #takes user to the main menu using magic method/dunders
    start()