#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 13:57:18 2019

@author: irinasm
"""

###   Making a Get request   ###

import requests
from requests.exceptions import HTTPError

url_01 = "http://df36c903.ngrok.io"
url_02 = "http://df36c903.ngrok.io/Molly"
url_03 = "http://df36c903.ngrok.io/query_example"
url_04 = "http://df36c903.ngrok.io/json_example"
url_05 = "http://df36c903.ngrok.io/answer_userID" #???

for url in [url_01, url_02, url_03, url_04, url_05]:
    try:
        response = requests.get(url)
        print ("The response is:", response)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        print ("The response status code is:", response.status_code)
        
        if response:
            print('Success!')
        else:
            print('An error has occurred.')
    
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
