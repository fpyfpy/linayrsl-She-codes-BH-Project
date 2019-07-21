#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 17:44:37 2019

@author: irinasm
"""

###   Making a Get request   ###

import requests
from requests.exceptions import HTTPError
url_01 = "http://7415f2b3.ngrok.io"



response = requests.post('https://httpbin.org/post', json={'key':'value'})
json_response = response.json()
json_response['data']'{"key": "value"}'
json_response['headers']['Content-Type']'application/json'