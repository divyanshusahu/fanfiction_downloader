#!/usr/bin/python3

import pdfkit
import sys
import os

def main() :

	if len(sys.argv) != 2 :
		print("./generate_pdf.py <filenane>")
		sys.exit()

	filename = sys.argv[1]
	with open(filename, 'rb') as f :
		text = f.read()
	text = text.decode("utf-8")
	#print(text)

	replace_dict = {'\n':'<br>'}
	data = text.replace('\n','<br>')
	
	options = {
		'page-size' : 'Letter',
		'margin-top' : '0.75in',
		'margin-right' : '0.75in',
		'margin-bottom' : '0.75in',
		'margin-left' : '0.75in',
		'encoding' : "UTF-8",
		'footer-center' : '[page] of [topage]'
	}

	newfile_name = filename.replace('.txt','.pdf')
	pdfkit.from_string(data, newfile_name, options=options)

	os.remove(filename)

if __name__ == '__main__':
	main()