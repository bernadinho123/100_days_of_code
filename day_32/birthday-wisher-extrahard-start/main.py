##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

files = ["letter_templates/letter_1.txt",
         "letter_templates/letter_2.txt",
         "letter_templates/letter_3.txt"]
my_email = "bemascarenhas6@gmail.com"
password = "mthvtrnksnqqlgjl"
# with open("letter_templates/letter_1.txt","r") as letter:
#     let = letter.read()
#
# print(let)
# cu = let.replace("[NAME]", "nome")
# print(cu)
# # with open("letter_templates/letter_1.txt", "w") as letter:
# #     letter.write(let)
# # print(let)
now = dt.datetime.now()
data_file = pandas.read_csv("birthdays.csv")
for file in range(len(data_file)):
    if data_file.year[file] == now.year:
        if data_file.month[file] == now.month:
            if data_file.day[file] == now.day:
                letter_use = random.choice(files)
                with open(letter_use, "r") as letter:
                    let = letter.read()
                new_let = let.replace("[NAME]", f"{data_file.name[file]}")
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email, to_addrs=data_file.email[file],
                                        msg=f"Subject:Happy Birthday\n\n{new_let}")

