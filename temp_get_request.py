#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 14:20:06 2019

@author: irinasm
"""

### TEMP ###
###   Making a Get request   ###

import requests

r = requests.get('https://api.github.com')
print (r)

if r:
    print('Success!')
else:
    print('An error has occurred.')
    

# ispol'zovanie response kak boolean (200-400=True, ostal'noe = False)
if response:
    print('Success!')
else:
    print('An error has occurred.')
   
# 2j sposob
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.') 
