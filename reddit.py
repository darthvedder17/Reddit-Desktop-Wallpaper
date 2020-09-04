import praw
import requests
from credentials import *
import json
from PIL import Image
import random
import ctypes
import urllib
def background_image(reddit):

	# img = Image.open
	reddit_bucket = []
	subreddit_name = input('Enter the name of the subreddit you want to download from : ')
	if subreddit_name == '':
		subreddit_name='EarthPorn'
	elif subreddit_name == 'wallpapers':
		print('Imma stop you right there and ask you to think of some page that is not as generic as this one. Also this script does not work here')


	posts = reddit.subreddit(subreddit_name).random()
	reddit_bucket.append(posts)
	for post in reddit_bucket : 
		url  = post.url
		name_of_file = url.split('/')
		if len(name_of_file) == 0 :
			name_of_file = re.findall('/(.*?)',url)
		name_of_file = name_of_file[-1]
		if "." not in name_of_file:
			name_of_file += '.jpg'
	
	# print(name_of_file)
	r = requests.get(url)
	# print(url)

	# firstpos=url.rfind("/")
	
	# lastpos=len(url)

	# print(url[firstpos+1:lastpos])

	# Download the file to the containing folder
	with open(name_of_file,"wb") as f:
		
		f.write(r.content)
	

	# Looks for the absolute filepath and changes the desktop wallpaper
	ctypes.windll.user32.SystemParametersInfoW(20, 0, f"C:\\Users\\shaurya\\Reddit\\{name_of_file}" , 0)	
	print(reddit_bucket)
	



reddit = praw.Reddit(client_id=my_client_id, client_secret=my_client_secret, user_agent=my_user_agent)
background_image(reddit)