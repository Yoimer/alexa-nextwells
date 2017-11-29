import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session

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


@ask.launch

def new_game():

    welcome_msg = render_template('welcome')

    return question(welcome_msg)
    


@ask.intent("YesIntent")

def getData():

     sess = requests.Session()
     
     #url = 'https://iot-php.000webhostapp.com/whitelist.txt'
     
     url = 'http://castillolk.com.ve/proyectos/sms/alexa.php?sw=7'
     
     data = sess.get(url)
     
     print data.content
     
     print "next line is the statement"
     
     #return statement(data.content)
     return statement('Action has been taken')



'''@ask.intent("AnswerIntent", convert={'first': int, 'second': int, 'third': int})

def answer(first, second, third):

    winning_numbers = session.attributes['numbers']

    if [first, second, third] == winning_numbers:

        msg = render_template('win')

    else:

        msg = render_template('lose')

    return statement(msg)'''


@ask.intent("NoIntent")

def no_intent():
    
    bye_text = 'I am not sure why you asked me to run then, but okay... bye'
    
    return statement(bye_text)
    

if __name__ == '__main__':

    app.run(debug=True)
