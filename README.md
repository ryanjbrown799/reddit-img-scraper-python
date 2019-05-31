# reddit-img-scraper-python
reddit image scraper built in python

image scraper for reddit built in python

Basic reddit media scrapper. enter a subreddit to scrape, select how many posts, and select which category(hot, new, rising, controversial, top) to sort the posts by. Files will by downloaded to a folder called data that must be in the working directory

Currently, it will download whatever is returned from the posts url, this is used to download images, but if the post is a link it will download the html. If it is a link to an imgur album, the scrapper will read through the html file and find all the images in the album and download them. If the link is to gfycat, the scrapper will read through the html and find the .mp4 and download it. If the posts url is a .gifv, the scrapper will find and download the .mp4

requires python 2.7.16, praw, folder called data in working directory, reddit account

built off of this tutorial http://www.storybench.org/how-to-scrape-reddit-with-python/
