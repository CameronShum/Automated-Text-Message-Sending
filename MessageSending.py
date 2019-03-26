import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse


fin = open('info.txt', 'r')
lines = fin.readlines()

#text file parsing for temperature, humidity, pressure, tilt

def file_read(lookfor):
    i = 0
    num = ""
    index = lines[1].find('"'+lookfor+'":"')+len(lookfor)+4
    #finds the index of a string, adds the length of the string to get the index of the character that follows
    while lines[1][index+i] != '"':
        num += (lines[1][index+i])
        #stores all values after within "" into a string
        i+=1
    return (float(num))
    #returns a float for numerical operations




app = Flask(__name__)
#creates instance of Flask

@app.route('/sms', methods=['GET', 'POST'])
#allows for the GET and POST protocols to be accessed at localhost:5000/sms

def sms_reply():

    body = request.values.get('Body', None)
    #gets the body of the text message

    resp = MessagingResponse()

    resp.message(str(file_read(body)))
    #changes the content of MessagingResponse, must be a string

    return str(resp)
    #sends the message to the local server


if __name__ == '__main__':
    #starts the server
    app.run()
