#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 15:37:30 2019

@author: irinasm
"""

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = "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"

message = Mail(
    from_email='fpyfpy@gmail.com', ## from
    to_emails='fpyfpy@gmail.com',  ## to
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get(SENDGRID_API_KEY))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
   # print(e.message)
    print (e)