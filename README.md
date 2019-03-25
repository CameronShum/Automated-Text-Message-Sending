# Automated Text Message Manipulation Using Python

A program that reacts to incoming text message and sends appropriate data from a text file.

## Prerequisites
- Install the Twilio and Flask libraries in the activated environment

```
pip install twilio
```

```
pip install Flask
```

- A [Twilio](https://www.twilio.com/) account with a Twilio phone number 
- [Ngrok](https://ngrok.com/)

## Usage
1) Open MessageSending.py.
2) Open a seperate command prompt to tunnel the server to a webhook.
3) Navigate to the activated ngrok.exe environment, type 
```
$ngrok http 5000
```
4) Copy the forwarding address: http://<span></span>XXXXXXXX.ngrok.io
```
ngrok by @inconshreveable                                                                               (Ctrl+C to quit)

Session Status                online
Account                       Free (Plan: Your Name)
Version                       2.3.23
Region                        United States (us)
Web Interface                 http://111.1.1.1:1111
Forwarding                    http://XXXXXXXX.ngrok.io -> http://localhost:5000
Forwarding                    https://XXXXXXXX.ngrok.io -> http://localhost:5000

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```
5) Paste http://<span></span>XXXXXXXX.ngrok.<span>/<span>io**/sms** into the webhook in twilio under messaging.  
![alt text](https://raw.githubusercontent.com/CameronShum/Automated-Text-Message-Sending/master/Twilio%20Webhook.jpg "Entering Webhook")

6) Send any of the below to the Twilio Phone number
 - Temperature
 - Humidity
 - Tilt
 - Pressure
