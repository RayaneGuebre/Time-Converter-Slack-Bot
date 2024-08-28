import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import pytz
from datetime import datetime

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.command("/cet")
def repeat_text(ack, respond, command):
        # Acknowledge command request
        ack()
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
            "CLT" : "America/Santiago", 
        } 

        text = command['text']
        text = str(text)
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
            response = "Invalid Timezone"
    
    
        respond(response)

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()

    
