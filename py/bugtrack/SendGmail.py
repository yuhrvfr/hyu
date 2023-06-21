#!/usr/bin/env python3

# go over to gmail account to setup 2 factor authentication
# generate app pwd
# create a function to send Emails

import os
from email.message import EmailMessage
import ssl
import smtplib

email_sender ='yuhrvfr@gmail.com'
email_pwd = os.environ.get("GMAIL_PWD")
email_receiver = 'yuhrvfr@yahoo.com'

subject = 'Check out Open AI discussion'

body = f"""
Your task is to answer in a consistent style.

<child>: Teach me about patience.

<grandparent>: The river that carves the deepest \
valley flows from a modest spring; the \
grandest symphony originates from a single note; \
the most intricate tapestry begins with a solitary thread.

<child>: Teach me about resilience.

https://www.youtube.com/watch?v=g_j6ILT-X0k
"""

em = EmailMessage()
em["From"]=email_sender
em["To"]=email_receiver
em["Subject"]=subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_pwd)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
