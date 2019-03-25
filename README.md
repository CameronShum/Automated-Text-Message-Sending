# Automated-Text-Message-Sending

A method that reacts to incoming text message and sends appropriate data from a text file.

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
1) Start MessageSending.py.
2) Open a seperate command prompt to tunnel the server to a webhook.
3) Navigate to the folder that contains ngrok.exe, type 
```
$ngrok http 5000
```
4)
