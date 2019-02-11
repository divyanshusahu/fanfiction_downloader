#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import sys
import pdfkit

def download(url) :
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "lxml")
	title = soup.find("h2")
	print(title.text)
	summary = soup.find("div", {"class":"storysummary"})
	chapters = int(summary.find_all("a")[-3].text)
	summary = "<br><br>" + str(soup.find("div", {"class":"storysummary"})) + "<hr><br>"
	print("Downloading Chapter 1 out of %s" % (str(chapters))) 
	storytext = str(soup.find("div",{"id":"storyinnerbody"})) + "<hr><br>"

	for i in range(2,chapters+1) :
		cur_url = url[:-1] + "-%s/" % str(i)
		r = requests.get(cur_url)
		soup = BeautifulSoup(r.text, "lxml")
		storytext += str(soup.find("div",{"id":"storyinnerbody"})) + "<br><hr><br>"
		print("Downloading Chapter %s out of %s" % (str(i), str(chapters))) 
	
	print("Please Wait!")
	options = {
		'page-size' : 'Letter',
		'margin-top' : '0.75in',
		'margin-right' : '0.75in',
		'margin-bottom' : '0.75in',
		'margin-left' : '0.75in',
		'encoding' : "UTF-8",
		'footer-center' : '[page] of [topage]'
	}

	pdfkit.from_string(str(title)+summary+storytext, str(title.text)+".pdf", options=options)


download(sys.argv[1])