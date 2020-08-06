#!/usr/bin/env python

import smtplib
import sys
# from email.message import EmailMessage

email_id = sys.argv[1]
password = sys.argv[2]
receiver = sys.argv[3]
message = sys.argv[4]
# filename = sys.argv[4]
# with open(filename) as fp:
	"""Her we read the contents of a file to send it through the mail."""
	msg = EmailMessage()
	msg.set_content(fp.read())
def send_mail(email_id, password, receiver)
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(email_id, password)
server.sendmail(email_id, receiver, message)

server.quit()