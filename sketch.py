timezones = {
    "GMT" : "Europe/London",
    "CET" : "Europe/Paris",
    "EET" : "Europe/Athens",
    "MSK" : "Europe/Moscow",
    "EST" : "America/New_York",
    "CST" : "America/Chicago",
    "MST" : "America/Denver",
    "PST" : "America/Los_Angeles",
    "IST" : "Asia/Kolkata",
    "CST" : "Asia/Shanghai",
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
import pytz
from datetime import datetime
text = input("Time to CET\n")
text = text.split(" ")
time = text[0]
timezone = text[1]
timezone = timezone.upper();
if timezone in timezones:
    time = datetime.strptime(time, '%H:%M')
    timezone = timezones[timezone]
    time_cet = time.astimezone(pytz.timezone('Europe/Paris'))
    response = time_cet.strftime('%H:%M %Z')
    print(response)
else:
    print("Invalid Timezone")