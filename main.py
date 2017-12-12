import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session

from flask import Flask, abort, request 
import json

######################################
from flask import Flask

import json

import requests

import time

import unidecode
######################################


app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@app.route('/nodemcu') 
def nodemcu():
    lastvalue = request.args.get('lastvalue')
    if lastvalue == 'ON' or lastvalue == 'OFF':
        return lastvalue
    else:
        return 'OK'
	# here we want to get the value of user (i.e. ?user=some-value)
    #lastvalue = request.args.get('lastvalue')
    #return lastvalue

@ask.launch

def launch_app():

    welcome_msg = render_template('welcome')

    return statement(welcome_msg)
    

@ask.intent("TurnOnIntent")

def turn_on():

    if lastvalue == 'ON':
        turn_on_msg = "System is already ON. No action will be taken"
        return statement(turn_on_msg)
    else:
        sess = requests.Session()
        # sent ON to Nodemcu by sendind 7 to db on castillolk
        url = 'http://castillolk.com.ve/proyectos/sms/alexa.php?sw=7'
        data = sess.get(url)
        print data.content
        print "next line is the statement"
        turn_on_msg = "Turning system ON... It might take a few seconds, please wait."
        return statement(turn_on_msg)

@ask.intent("TurnOffIntent")

def turn_off():
    
    sess = requests.Session()

    # sent ON to Nodemcu by sendind 8 to db on castillolk
    url = 'http://castillolk.com.ve/proyectos/sms/alexa.php?sw=8'
     
    data = sess.get(url)
     
    print data.content
     
    print "next line is the statement"

    turn_on_msg = "Turning system OFF... It might take a few seconds, please wait."
     
    return statement(turn_on_msg)
    

if __name__ == '__main__':

    app.run(debug=True,  host='0.0.0.0')
