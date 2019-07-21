#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 15:15:03 2019

@author: irinasm
"""

### Hello, world!  ###
#from flask import Flask
#app = Flask(__name__)

#@app.route("/")
#def hello():
#    return "Hello World!"

#if __name__ == "__main__":
#    app.run()



### Hello s imenem ###
    
from flask import Flask
import requests
from flask import jsonify

app = Flask(__name__)


@app.route("/<username>", methods=['GET'])
def index(username):
    return "Hello, %s!" % username

@app.route("/answer_userID", methods=['GET']) #???????
def answer_userID():
    message = "OK"
    return message

@app.route("/query_example", methods=['GET'])
def query_example():
    language = request.args.get('language')

    framework = request.args['framework']
    website = request.args.get('website')
    return '''<h1>
            The language is: {}.
            The framework is: {}.
            The website is: {}</h1>'''.format(language, framework, website)
            
@app.route('/json_example', methods=['GET', 'POST'])
def json_example():
    req_data = request.get_json()
    now = datetime.now()
    year = now.year
    time = now.strftime("%H:%M:%S")
    day = now.dayw
    month = now.strftime('%b')
    date = '{} {} {}'.format(day, month.upper(), year)
    my_id = req_data['ID']
    first_name = req_data['firstName']
    last_name = req_data['lastName']

    my_gedcom = '''
    1 DATE {}\n
    2 TIME {}\n
    1 FILE base.ged.tmp\n
    1 GEDC\n
    2 VERS 5.5\n
    2 FORM LINEAGE-LINKED\n
    1 CHAR ASCII\n
    0 @{}@ INDI\n
    1 NAME {} /{}\n
    1 OBJE\n
    2 FILE'''.format(date, time, my_id, first_name, last_name)

    return my_gedcom

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)

