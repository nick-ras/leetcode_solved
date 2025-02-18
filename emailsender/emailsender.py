import os
from email.message import EmailMessage
import ssl
import smtplib

class emails():

	def send_welcome_email(self):
		email_sender = 'ttestesen81@gmail.com'
		email_password= os.getenv('emailsender_pass')
		email_reciever = "email"

		em = EmailMessage()
		subject = ''
		body = """"""

		em['From'] = email_sender
		em['To'] = email_reciever
		em['Subject'] = subject
		em.set_content(body)
		context = ssl.create_default_context()
		subject = 'welcome'
		body = """welcome to automation"""
		with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
			smtp.login(email_sender, email_password)
			smtp.sendmail(email_sender, email_reciever, em.as_string())
