import datetime
now = datetime.datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S.%f")
print(formatted_date)