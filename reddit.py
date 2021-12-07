import praw
import requests
from credentials import *
import ctypes
import logging
import os,sys
from argparse import ArgumentParser
import time
base_dir = os.getcwd()
sys.path.append(base_dir)
message = []
err_count = 0
log_dir = "logs"
log_file = "std.log"
log_file_path = f'{base_dir}//{log_dir}'
if not os.path.exists(log_file_path): 
	os.makedirs(log_file_path)
	file = open(log_file, 'a').close()
logging.basicConfig(filename=f'{log_file_path}//{log_file}', 
					format='%(asctime)s %(message)s', 
					filemode='w') 
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 
class Reddit:
	def background_image(self,reddit,subreddit_name,base_directory):
		global err_count
		global base_dir
		try:
			reddit_bucket = []
			if not subreddit_name:
				subreddit_name='EarthPorn'
			elif subreddit_name == 'wallpapers':
				print('Imma stop you right there and ask you to think of some page that is not as generic as this one. Also this script does not work here')
				return -1
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
			r = requests.get(url)
			if not base_directory:
				base_directory = base_dir
			dir = "Wallpapers"
			path = os.path.join(base_directory,dir)
			os.mkdir(path)
			print(f"Wallpaper saved in {path}")
			with open(f"{path}\\{name_of_file}","wb") as f:
					f.write(r.content)
			'''Looks for the absolute filepath and changes the desktop wallpaper'''
			ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{path}\\{name_of_file}" , 0)	
			print(reddit_bucket)
		except Exception as e:
			err_count+=1
			logger.error(e) 
			
if __name__ == '__main__':
	parser = ArgumentParser()
	parser.add_argument('-dl', '--dl',
						required=False,
						type=str,
						help='Specify the download location of the wallpapers you want to use'
						)    
	args = parser.parse_args()
	script_start_time = time.time()
	subreddit_name = input('Enter the name of the subreddit you want to download from (default subreddit = EarthPorn): ')
	reddit_obj = Reddit()
	reddit = praw.Reddit(client_id=my_client_id, client_secret=my_client_secret, user_agent=my_user_agent)
	reddit_obj.background_image(reddit,subreddit_name,args.dl)
	if err_count == 0 :
		logger.info("Wallpaper downloaded successfully!")



