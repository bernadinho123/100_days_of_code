import smtplib
import datetime as dt
import random

my_email = "bemascarenhas6@gmail.com"
password = "mthvtrnksnqqlgjl"


now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 1:
    with open("quotes.txt", "r") as data_file:
        data = data_file.readlines()
        text = random.choice(data)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="amfonseca2005@gmail.com",
                                msg=f"Subject:Motivation\n\n{text}")

