#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import sys
import pdfkit
import binascii

ROOT_URL = "https://harrypotterfanfiction.com"

def download(url) :
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "lxml")
	summary = soup.find("section",{"class":"section--2"})
	summary = summary.find_all("div",{"class","row"})[1]
	top_details = soup.find("div",{"class":"section__content section__content--viewstory-page"})
	title = top_details.find("h2").text
	title = title.split("\n")[1][16:]
	print("Downloading %s" % (title))
	chapters = int(top_details.find_all("dd")[1].text)
	chapters_list = soup.find("div",{"class":"section__inner"})
	chapters_url = chapters_list.find_all("a",{"class":"h4"})

	whole_story = str(top_details) + str(summary) + "<br><br><hr><br><br>" + str(chapters_list) + "<br><br><hr><br><br>"

	cur = 1
	for c in chapters_url :
		u = ROOT_URL + c["href"]
		ct = c.text
		print("Downloading chapter %s of %s" % (cur, chapters))
		r1 = requests.get(u)
		s1 = BeautifulSoup(r1.text, "lxml")
		c_text = "<h3>%s</h3>" % (str(ct))
		c_text += str(s1.find("div",{"class":"storytext-container"}))
		c_text += "<br><br><hr><br><br>"
		#print(c_text)
		whole_story += c_text
		cur += 1

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
	pdfkit.from_string(whole_story, title+".pdf", options=options)


download(sys.argv[1])