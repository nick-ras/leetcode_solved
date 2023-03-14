from datetime import datetime
import time
import hashlib
from urllib.request import urlopen, Request
from emailsender import emails
import os
import requests

class website_check():
	def check_changes(self):
		url = requests.get('https://www.dr.dk')
		hash = hashlib.sha256()
		hash.update(url.text.encode('utf-8'))
		while True:
			print("running")
			try:
				url2 = requests.get('https://www.dr.dk')
				hash2 = hashlib.sha256()
				hash2.update(url2.text.encode('utf-8'))
				if (hash.hexdigest() != hash2.hexdigest()):
					print("changed")
					# emails().send_welcome_email()
					hash = hash2
				else:
					print("not changed")
			except Exception as e:
				print("error")
				exit(2)
			time.sleep(2)
		return response

check = website_check().check_changes()

print(check)

