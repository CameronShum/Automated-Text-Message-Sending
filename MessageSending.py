import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse


fin = open('info.txt', 'r')
lines = fin.readlines()

#text file parsing for temperature, humidity, pressure, tilt

def temp_read():
    i = 0
    num = ""
    index = lines[1].find('"Temperature":"')+15
    #finds the index of a string, adds the length of the string to get the index of the character that follows
    while lines[1][index+i] != '"':
        num += (lines[1][index+i])
        #stores all values after within "" into a string
        i+=1
    return (float(num))
    #returns a float for numerical operations


def humi_read():
    i = 0
    num = ""
    index = lines[1].find('"Humidity":"')+12
    while lines[1][index+i] != '"':
        num += (lines[1][index+i])
        i+=1
    return (float(num))

def pres_read():
    i = 0
    num = ""
    index = lines[1].find('"Pressure":"')+12
    while lines[1][index+i] != '"':
        num += (lines[1][index+i])
        i+=1
    return (float(num))

def tilt_read():
    i = 0
    num = ""
    index = lines[1].find('"Tilt":"')+8
    while lines[1][index+i] != '"':
        num += (lines[1][index+i])
        i+=1
    return (float(num))




app = Flask(__name__)
#creates instance of Flask

@app.route('/sms', methods=['GET', 'POST'])
#allows for the GET and POST protocols to be accessed at localhost:5000/sms

def sms_reply():

    body = request.values.get('Body', None)
    #gets the body of the text message

    resp = MessagingResponse()

    if body == "Tilt":
        resp.message(str(tilt_read()))
        #changes the content of MessagingResponse, must be a string

    if body == "Pressure":
        resp.message(str(pres_read()))

    if body == "Temperature":
        resp.message(str(temp_read()))

    if body == "Humidity":
        resp.message(str(humi_read()))

    return str(resp)
    #sends the message to the local server


if __name__ == '__main__':
    #starts the server
    app.run()
