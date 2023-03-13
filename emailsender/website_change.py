from datetime import datetime
import time
import hashlib
from urllib.request import urlopen, Request
from developit import emails

class website_check():
	def check_changes(self):
		url = Request('https://youtube.com/',
									headers={'User-Agent': 'Mozilla/5.0'})
		response = urlopen(url).read()
		currentHash = hashlib.sha224(response).hexdigest()
		print("running")
		time.sleep(10)
		while True:
			try:
				# perform the get request and store it in a var
				response = urlopen(url).read()
				currentHash = hashlib.sha224(response).hexdigest()
				time.sleep(30)
				response = urlopen(url).read()
				newHash = hashlib.sha224(response).hexdigest()
				if newHash == currentHash:
					continue
				else:
					emails().send_welcome_email()
					response = urlopen(url).read()
					currentHash = hashlib.sha224(response).hexdigest()
					time.sleep(2)
					continue
			except Exception as e:
					print("error")

check = website_check().check_changes()

print("hello world")
print(os.environ)
check()
