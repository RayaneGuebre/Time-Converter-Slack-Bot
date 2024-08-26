import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
from pytz import timezone

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
 
app = Flask(__name__)

client.chat_postMessage(channel='#timezone-bot-test', text="I'M ALIVE")


@app.route('/cet', methods=['GET','POST'])
def cet():
    data = request.form
    user_id = data.get('user_id')
    command_text = data.get('text')
    channel_id = data.get('channel_id')
    
    text = command_text.split(" ")
    time = text[0]
    timezone = text[1]
    timezone = timezone.upper();


    response = hours + "in" + timezone + "--->"
    time_cet = time.astimezone(timezone('Europe/Rome'))
    
    client.chat_postMessage(channel=channel_id, text=response)
    return Response(), 200
@app.route('/gmt', methods=['GET','POST'])
def gmt():
    data = request.form
    user_id = data.get('user_id')
    command_text = data.get('text')
    channel_id = data.get('channel_id')
    
    text = command_text.split(" ")
    time = text[0]
    timezone = text[1]
    timezone = timezone.upper();


    response = hours + "in" + timezone + "--->"
    time_cet = time.astimezone(timezone('Europe/London'))
    
    client.chat_postMessage(channel=channel_id, text=response)
    return Response(), 200






if __name__ == "__main__":
    app.run(debug=True)
