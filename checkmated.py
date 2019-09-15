import requests

"""for i in range(1,10000) :
	url = "https://web.archive.org/web/submit?url=http://checkmated.com/story.php?story=%s&type=replay" % (str(i))
	r = requests.get(url)
	if r.status_code == 200 :
		print i"""

i = 301
while True :
	
	url = "https://web.archive.org/web/submit?url=http://checkmated.com/story.php?story=%s&type=replay" % (str(i))
	r = requests.get(url)
	if r.status_code == 200 :
		print i

	if i % 10 == 0 :
		c = raw_input("Continue(Y/N): ")
		if c.lower() == "n" :
			break
	
	i += 1
