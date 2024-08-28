import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import pytz
from datetime import datetime

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

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.command("/cet")
def repeat_text(ack, respond, command):
        # Acknowledge command request
        ack()
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
            

            now = datetime.now()
            time = time.replace(year=now.year, month=now.month, day=now.day)
    
            choosed_timezone = pytz.timezone(timezones[timezone])
        
    
            choosed_time = choosed_timezone.localize(time)
            
    
            cet_timezone = pytz.timezone('Europe/Paris')
            
    
            time_cet = choosed_time.astimezone(cet_timezone)
    
            response = time_cet.strftime('%H:%M %Z')
        
        else:
            response = "Invalid Timezone"
    
    
        respond(response)


@app.command("/gmt")
def repeat_text(ack, respond, command):
        # Acknowledge command request
        ack()
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
            

            now = datetime.now()
            time = time.replace(year=now.year, month=now.month, day=now.day)
    
            choosed_timezone = pytz.timezone(timezones[timezone])
            
    
            choosed_time = choosed_timezone.localize(time)
            
    
            gmt_timezone = pytz.timezone('Europe/London')
    
            time_gmt = choosed_time.astimezone(gmt_timezone)
    
            response = time_gmt.strftime('%H:%M %Z')
        
        else:
            response = "Invalid Timezone"
    
    
        respond(response)
@app.command("/eet")
def repeat_text(ack, respond, command):
        # Acknowledge command request
        ack()
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
        

            now = datetime.now()
            time = time.replace(year=now.year, month=now.month, day=now.day)
    
            choosed_timezone = pytz.timezone(timezones[timezone])
            
    
            choosed_time = choosed_timezone.localize(time)
            
    
            eet_timezone = pytz.timezone('Europe/Athens')

    
            time_eet = choosed_time.astimezone(eet_timezone)
    
            response = time_eet.strftime('%H:%M %Z')
            
        else:
            response = "Invalid Timezone"
    
    
        respond(response)
@app.command("/msk")
def repeat_text(ack, respond, command):
        # Acknowledge command request
        ack()
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
            

            now = datetime.now()
            time = time.replace(year=now.year, month=now.month, day=now.day)
    
            choosed_timezone = pytz.timezone(timezones[timezone])
            
    
            choosed_time = choosed_timezone.localize(time)
            
    
            msk_timezone = pytz.timezone('Europe/Moskow')
            
    
            time_msk = choosed_time.astimezone(msk_timezone)
    
            response = time_msk.strftime('%H:%M %Z')
        else:
            response = "Invalid Timezone"
    
    
        respond(response)

@app.command("/est")
def repeat_text(ack, respond, command):
        # Acknowledge command request
        ack()
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
            

            now = datetime.now()
            time = time.replace(year=now.year, month=now.month, day=now.day)
    
            choosed_timezone = pytz.timezone(timezones[timezone])
            
    
            choosed_time = choosed_timezone.localize(time)
            
    
            est_timezone = pytz.timezone('America/New_York')
            
    
            time_est = choosed_time.astimezone(est_timezone)
    
            response = time_est.strftime('%H:%M %Z')
        else:
            response = "Invalid Timezone"
    
    
        respond(response) 

@app.command("/cstUS")
def repeat_text(ack, respond, command):
        # Acknowledge command request
        ack()
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
            

            now = datetime.now()
            time = time.replace(year=now.year, month=now.month, day=now.day)
    
            choosed_timezone = pytz.timezone(timezones[timezone])
            
    
            choosed_time = choosed_timezone.localize(time)
            
    
            cst_us_timezone = pytz.timezone('America/Chicago')
            
    
            time_cst_us = choosed_time.astimezone(cst_us_timezone)
    
            response = time_cst_us.strftime('%H:%M %Z')
        else:
            response = "Invalid Timezone"
    
    
        respond(response)
@app.command("/mst")
def repeat_text(ack, respond, command):
        # Acknowledge command request
        ack()
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
            

            now = datetime.now()
            time = time.replace(year=now.year, month=now.month, day=now.day)
    
            choosed_timezone = pytz.timezone(timezones[timezone])
            
    
            choosed_time = choosed_timezone.localize(time)
            
    
            mst_timezone = pytz.timezone('America/Denver')
            
    
            time_mst = choosed_time.astimezone(mst_timezone)
    
            response = time_mst.strftime('%H:%M %Z')
        else:
            response = "Invalid Timezone"
    
    
        respond(response)
@app.command("/msk")
def repeat_text(ack, respond, command):
        # Acknowledge command request
        ack()
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
            

            now = datetime.now()
            time = time.replace(year=now.year, month=now.month, day=now.day)
    
            choosed_timezone = pytz.timezone(timezones[timezone])
            
    
            choosed_time = choosed_timezone.localize(time)
            
    
            msk_timezone = pytz.timezone('Europe/Moskow')
            
    
            time_msk = choosed_time.astimezone(msk_timezone)
    
            response = time_msk.strftime('%H:%M %Z')
        else:
            response = "Invalid Timezone"
    
    
        respond(response)
@app.command("/pst")
def repeat_text(ack, respond, command):
        # Acknowledge command request
        ack()
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
            

            now = datetime.now()
            time = time.replace(year=now.year, month=now.month, day=now.day)
    
            choosed_timezone = pytz.timezone(timezones[timezone])
            
    
            choosed_time = choosed_timezone.localize(time)
            
    
            pst_timezone = pytz.timezone('America/Los_Angeles')
            
    
            time_pst = choosed_time.astimezone(pst_timezone)
    
            response = time_pst.strftime('%H:%M %Z')
        else:
            response = "Invalid Timezone"
    
    
        respond(response)
@app.command("/ist")
def repeat_text(ack, respond, command):
        # Acknowledge command request
        ack()
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
            

            now = datetime.now()
            time = time.replace(year=now.year, month=now.month, day=now.day)
    
            choosed_timezone = pytz.timezone(timezones[timezone])
            
    
            choosed_time = choosed_timezone.localize(time)
            
    
            ist_timezone = pytz.timezone('Asia/Kolkata')
            
    
            time_ist = choosed_time.astimezone(ist_timezone)
    
            response = time_ist.strftime('%H:%M %Z')
        else:
            response = "Invalid Timezone"
    
    
        respond(response)

@app.command("/cstCN")
def repeat_text(ack, respond, command):
        # Acknowledge command request
        ack()
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
            

            now = datetime.now()
            time = time.replace(year=now.year, month=now.month, day=now.day)
    
            choosed_timezone = pytz.timezone(timezones[timezone])
            
    
            choosed_time = choosed_timezone.localize(time)
            
    
            cst_cn_timezone = pytz.timezone('Asia/Shanghai')
            
    
            time_cst_cn = choosed_time.astimezone(cst_cn_timezone)
    
            response = time_cst_cn.strftime('%H:%M %Z')
        else:
            response = "Invalid Timezone"
    
    
        respond(response)

@app.command("/jst")
def repeat_text(ack, respond, command):
        # Acknowledge command request
        ack()
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
            

            now = datetime.now()
            time = time.replace(year=now.year, month=now.month, day=now.day)
    
            choosed_timezone = pytz.timezone(timezones[timezone])
            
    
            choosed_time = choosed_timezone.localize(time)
            
    
            jst_timezone = pytz.timezone('Asia/Japan')
            
    
            time_jst = choosed_time.astimezone(jst_timezone)
    
            response = time_jst.strftime('%H:%M %Z')
        else:
            response = "Invalid Timezone"
    
    
        respond(response)
@app.command("/aest")
def repeat_text(ack, respond, command):
        # Acknowledge command request
        ack()
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
            

            now = datetime.now()
            time = time.replace(year=now.year, month=now.month, day=now.day)
    
            choosed_timezone = pytz.timezone(timezones[timezone])
            
    
            choosed_time = choosed_timezone.localize(time)
            
    
            aest_timezone = pytz.timezone('Australia/Sydney')
            
    
            time_aest = choosed_time.astimezone(aest_timezone)
    
            response = time_aest.strftime('%H:%M %Z')
        else:
            response = "Invalid Timezone"
    
    
        respond(response)

@app.command("/nzst")
def repeat_text(ack, respond, command):
        # Acknowledge command request
        ack()
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
            

            now = datetime.now()
            time = time.replace(year=now.year, month=now.month, day=now.day)
    
            choosed_timezone = pytz.timezone(timezones[timezone])
            
    
            choosed_time = choosed_timezone.localize(time)
            
    
            nzst_timezone = pytz.timezone('Pacific/Auckland')
            
    
            time_nzst = choosed_time.astimezone(nzst_timezone)
    
            response = time_nzst.strftime('%H:%M %Z')
        else:
            response = "Invalid Timezone"
    
    
        respond(response)

@app.command("/sast")
def repeat_text(ack, respond, command):
        # Acknowledge command request
        ack()
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
            

            now = datetime.now()
            time = time.replace(year=now.year, month=now.month, day=now.day)
    
            choosed_timezone = pytz.timezone(timezones[timezone])
            
    
            choosed_time = choosed_timezone.localize(time)
            
    
            sast_timezone = pytz.timezone('Africa/Johannesburg')
            
    
            time_sast = choosed_time.astimezone(sast_timezone)
    
            response = time_sast.strftime('%H:%M %Z')
        else:
            response = "Invalid Timezone"
    
    
        respond(response)

@app.command("/wat")
def repeat_text(ack, respond, command):
        # Acknowledge command request
        ack()
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
            

            now = datetime.now()
            time = time.replace(year=now.year, month=now.month, day=now.day)
    
            choosed_timezone = pytz.timezone(timezones[timezone])
            
    
            choosed_time = choosed_timezone.localize(time)
            
    
            wat_timezone = pytz.timezone('Africa/Lagos')
            
    
            time_wat = choosed_time.astimezone(wat_timezone)
    
            response = time_wat.strftime('%H:%M %Z')
        else:
            response = "Invalid Timezone"
    
    
        respond(response)

@app.command("/ast")
def repeat_text(ack, respond, command):
        # Acknowledge command request
        ack()
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
            

            now = datetime.now()
            time = time.replace(year=now.year, month=now.month, day=now.day)
    
            choosed_timezone = pytz.timezone(timezones[timezone])
            
    
            choosed_time = choosed_timezone.localize(time)
            
    
            ast_timezone = pytz.timezone('Asia/Riyadh')
            
    
            time_ast = choosed_time.astimezone(ast_timezone)
    
            response = time_ast.strftime('%H:%M %Z')
        else:
            response = "Invalid Timezone"
    
    
        respond(response)

@app.command("/art")
def repeat_text(ack, respond, command):
        # Acknowledge command request
        ack()
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
            

            now = datetime.now()
            time = time.replace(year=now.year, month=now.month, day=now.day)
    
            choosed_timezone = pytz.timezone(timezones[timezone])
            
    
            choosed_time = choosed_timezone.localize(time)
            
    
            art_timezone = pytz.timezone('America/Argentina/Buenos_Aires')
            
    
            time_art = choosed_time.astimezone(art_timezone)
    
            response = time_art.strftime('%H:%M %Z')
        else:
            response = "Invalid Timezone"
    
    
        respond(response)
    
@app.command("/msk")
def repeat_text(ack, respond, command):
        # Acknowledge command request
        ack()
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
            

            now = datetime.now()
            time = time.replace(year=now.year, month=now.month, day=now.day)
    
            choosed_timezone = pytz.timezone(timezones[timezone])
            
    
            choosed_time = choosed_timezone.localize(time)
            
    
            brt_timezone = pytz.timezone('America/San_Paulo')
            
    
            time_brt = choosed_time.astimezone(brt_timezone)
    
            response = time_brt.strftime('%H:%M %Z')
        else:
            response = "Invalid Timezone"
    
    
        respond(response)

@app.command("/clt")
def repeat_text(ack, respond, command):
        # Acknowledge command request
        ack()
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
            

            now = datetime.now()
            time = time.replace(year=now.year, month=now.month, day=now.day)
    
            choosed_timezone = pytz.timezone(timezones[timezone])
            
    
            choosed_time = choosed_timezone.localize(time)
            
    
            clt_timezone = pytz.timezone('America/Santiago')
            
    
            time_clt = choosed_time.astimezone(clt_timezone)
    
            response = time_clt.strftime('%H:%M %Z')
        else:
            response = "Invalid Timezone"
    
    
        respond(response)

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()

    

    
