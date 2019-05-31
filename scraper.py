import praw
import urllib
import os

cwd = os.getcwd()

#connect to reddit
reddit = praw.Reddit(client_id='PERSONAL_USE_SCRIPT_14_CHARS',
					client_secret='SECRET_KEY_27_CHARS',
					password='YOUR_APP_NAME',
					user_agent='YOUR_REDDIT_USER_NAME',
					username='YOUR_REDDIT_LOGIN_PASSWORD')
	
#check if connection worked
print(reddit.user.me())

print("subreddit to scrape?")
subScrap = raw_input()

print("amount of posts to scrape?")
num = raw_input()
num = int(num)

subreddit = reddit.subreddit(subScrap)

print("category:\n (1) top\n (2) new\n (3) hot\n (4) controversial\n (5) rising")
cat = raw_input()
if cat =='1':
	sel_subreddit = subreddit.top(limit=num)
if cat =='2':
	sel_subreddit = subreddit.new(limit=num)
if cat =='3':
	sel_subreddit = subreddit.hot(limit=num)
if cat =='4':
	sel_subreddit = subreddit.controversial(limit=num)
if cat =='5':
	sel_subreddit = subreddit.rising(limit=num)

	
topics_dict = { "url":[]  
              }

#get urls for posts			  
for submission in sel_subreddit:
    topics_dict["url"].append(submission.url)



#loop through urls and try to download them to /data/
for x in topics_dict["url"]:
	print(x)
	filename = x.split('/')[-1]
	filename = filename.split('?')
	filename = cwd + '/data/' + filename[0]
	
	#download from given url
	try: urllib.urlretrieve(x, filename)
	
	except:
		print("error could not download {} ".format(x))
		continue
		
	#if .gifv open the downloaded .gifv file and find the .mp4 url in the html and download it then delete the .gifv 
	if filename.split('.')[-1] == "gifv":
		with open(filename) as f:
			datafile = f.readlines()
		search ='<meta itemprop="contentURL" '
		for line in datafile:
			if search in line:
				newStr = line.replace(" ","").split('"')
				for y in newStr:
					if '.mp4' in y:
						print(y)
						fileN = y.split('/')[-1]
						fileN = fileN.split('?')
						fileN = cwd + '/data/' + fileN[0]
						try: urllib.urlretrieve(y, fileN)
						
						except:
							print("error could not download {} ".format(y))
							os.remove(filename)
							f.close()
							continue
		
		f.close()
		os.remove(filename)
	
	#if link is gfycat search the downloaded html file for the url for the .mp4, download it, then delete the html file
	if 'gfycat.com' in x.split("/"):
		with open(filename) as f:
			datafile = f.readlines()
		search1 ='<source src="https://giant.gfycat.com/'
		search2 ='<source src="https://fat.gfycat.com/'
		search3 ='<source src="https://zippy.gfycat.com/'

		for line in datafile:
			if search1 in line or search2 in line or search3 in line:
				st = line.find('source src=')
				en = line.find('type="video/mp4"/>')
				newLine = line[st:en]
				
				newLine = newLine.replace(" ","").split("=")[-1].strip('"')
				
				fileN = newLine.split('/')[-1]
				fileN = fileN.split('?')
				fileN = cwd + '/data/' + fileN[0]
				try: urllib.urlretrieve(newLine, fileN)
										
				except:
					print("error could not download {} ".format(newLine))
					os.remove(filename)
					f.close()
					continue
		
		f.close()		
		os.remove(filename)
		
	#check if link to imgur album, find and download all photos in album, delete html file after
	if 'imgur.com' in x.split("/"):
		with open(filename) as f:
			datafile = f.readlines()
		search ='class="post-image-container'
		for line in datafile:
			if search in line:
				newLine = (line.split('=')[1]).split(" ")[0].strip('"')
				newLine = 'https://i.imgur.com/'+newLine+'.jpg'
				
				print(newLine)

				fileN = newLine.split('/')[-1]
				fileN = fileN.split('?')
				fileN = cwd + '/data/' + fileN[0]
				try: urllib.urlretrieve(newLine, fileN)
										
				except:
					print("error could not download {} ".format(newLine))
					os.remove(filename)
					f.close()
					continue
		f.close()
		os.remove(filename)













	
	