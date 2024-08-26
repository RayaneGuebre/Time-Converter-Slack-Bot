text = input("Time to CET")
text = text.split(" ")
time = text[0]
timezone = text[1]
timezone = timezone.upper();
time_cet = time.astimezone(timezone('Europe/Rome'))
response = time_cet
print(response)