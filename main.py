import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session

######################################
from flask import Flask

import json

import requests

######################################


app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch

def launch_app():

    welcome_msg = render_template('welcome')

    return statement(welcome_msg)
    

@ask.intent("OnIntent")

def turn_on():
    
    #global sw
    #time.sleep(2)
    
	sess = requests.Session()

	url = 'http://castillolk.com.ve/proyectos/sms/alexa.php?'
     
	data = sess.get(url)
     
	print data.content

    #if sw == '7':
	if 'ON' in data.content:

	    turn_on_msg = "System is already turned on. Not action taken."

	    print(turn_on_msg)

	    return statement(turn_on_msg)

	else:
	    sess = requests.Session()

	    # sent ON to Nodemcu by sendind 7 to db on castillolk
	    url = 'http://castillolk.com.ve/proyectos/sms/alexa.php?sw=7'
     
	    data = sess.get(url)
     
	    print data.content
     
	    print "next line is the statement"

	    turn_on_msg = "Turning system ON... It might take a few seconds, please wait."
        
	    print(turn_on_msg)
		
	    return statement(turn_on_msg)


@ask.intent("OffIntent")

def turn_off():
    
    #global sw
    #time.sleep(2)

	sess = requests.Session()

	url = 'http://castillolk.com.ve/proyectos/sms/alexa.php?'
     
	data = sess.get(url)
     
	print data.content

    #if sw == '8':
	if 'OFF' in data.content:

	    turn_off_msg = "System is already turned off. Not action taken."

	    print(turn_off_msg)

	    return statement(turn_off_msg)

	else:
	    sess = requests.Session()

        # sent ON to Nodemcu by sendind 8 to db on castillolk
        url = 'http://castillolk.com.ve/proyectos/sms/alexa.php?sw=8'
     
        data = sess.get(url)
     
        print data.content
     
        print "next line is the statement"

        turn_on_msg = "Turning system OFF... It might take a few seconds, please wait."

        #sw = '8'
        print(turn_on_msg)
     
        return statement(turn_on_msg)
    

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')