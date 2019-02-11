#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import optparse
import sys
import os
import pdfkit

ROOT_URL = "https://www.fanfiction.net/s/"

def downloader(id) :
	r = requests.get(ROOT_URL + id + "/1/")
	
	if r.status_code == 404 :
		print('Not found!')
		os._exit(0)

	soup = BeautifulSoup(r.text, "lxml")
	fic_info = soup.find("div",{'id' : 'profile_top'})
	
	fic_title = fic_info.find_all("b")[0].text
	fic_author = fic_info.find_all("a")[0].text
	fic_summary = fic_info.find_all("div")[1].text
	#fic_rating = fic_info.find_all("a")[2].text
	fic_status = fic_info.find("span",{'class' : 'xgray xcontrast_txt'}).text

	fic_page1 = "<b>Title : </b>" + fic_title + "<br><br>" + "<b>Author : </b>" + fic_author + "<br><br>" + "<b>Summary : </b>" + fic_summary + "<br><br>" + fic_status + "<br><br><hr>"
	#print(fic_page1)

	#pdfkit.from_string(fic_page1, fic_title)
	try :
		no_of_chapters = len(soup.find("select").find_all("option"))

	except :
		no_of_chapters = 1
	
	story_text = ""
	print("Downloading " + fic_title)

	for i in range(1,no_of_chapters+1) :
		#print(ROOT_URL+id+"/"+str(i)+"/")
		r2 = requests.get(ROOT_URL+id+"/"+str(i)+"/")
		soup2 = BeautifulSoup(r2.text, "lxml")
		#chapter_text = str(soup2.find("div", {"id": "storytext"}))
		story_text += "<h2>Chapter %s </h2><br>" % (str(i))
		story_text += str(soup2.find("div", {'id' : 'storytext'})) + "<br><br> End of the chapter <br><br><hr><br><br>"
		#print('*', end='')
		#print(str((i/no_of_chapters)*100) + " %")
		print("Chapter " + str(i) + " of " + str(no_of_chapters))
		#print(str(story_text))
	
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
	pdfkit.from_string(fic_page1 + story_text, fic_author + "-" + fic_title+".pdf", options=options)


def main() :
	if len(sys.argv) != 2 :
		print("./download.py <story_id>")
		os._exit(0)
	
	STORY_ID = sys.argv[1]
	downloader(STORY_ID)


if __name__ == '__main__' :

	main()
