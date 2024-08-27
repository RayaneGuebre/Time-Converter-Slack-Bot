import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
from pytz import timezone
import pytz
from datetime import datetime

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
 
app = Flask(__name__)

client.chat_postMessage(channel='#timezone-bot-test', text="I'M ALIVE")

timezones = {
    "GMT" : "Europe/London",
    "CET" : "Europe/Paris",
    "EET" : "Europe/Athens",
    "MSK" : "Europe/Moscow",
    "EST" : "America/New_York",
    "CST_US" : "America/Chicago",
    "MST" : "America/Denver",
    "PST" : "America/Los_Angeles",
    "IST" : "Asia/Kolkata",
    "CST_CN " : "Asia/Shanghai",
    "JST" : "Asia/Tokyo",
    "AEST" : "Australia/Sydney",
    "NZST" : "Pacific/Auckland",
    "SAST" : "Africa/Johannesburg",
    "WAT" : "Africa/Lagos",
    "AST" : "Asia/Riyadh",
    "ART" : "America/Argentina/Buenos_Aires",
    "BRT" : "America/Sao_Paulo",
    "CLT" : "Santiago", 
} 



@app.route('/cet', methods=['GET','POST'])
def cet():
    data = request.form
    user_id = data.get('user_id')
    command_text = data.get('text')
    channel_id = data.get('channel_id')
    
    text = input("Time to CET\n")
    if "." in text:
        text = text.replace(".", ":")
    text = text.split(" ")
    time = text[0]
    timezone = text[1]
    timezone = timezone.upper();
    if timezone in timezones:

        time = datetime.strptime(time, '%H:%M')
        print(time)

        now = datetime.now()
        time = time.replace(year=now.year, month=now.month, day=now.day)
    
        choosed_timezone = pytz.timezone(timezones[timezone])
        print(choosed_timezone)
    
        choosed_time = choosed_timezone.localize(time)
        print(choosed_time)
    
        cet_timezone = pytz.timezone('Europe/Paris')
        print(cet_timezone)
    
        time_cet = choosed_time.astimezone(cet_timezone)
    
        response = time_cet.strftime('%H:%M %Z')
        print(response)
    else:
        print("Invalid Timezone")
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
