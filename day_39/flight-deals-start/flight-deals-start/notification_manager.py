import smtplib


class NotificationManager:
    def __init__(self):
        self.my_email = "bemascarenhas6@gmail.com"
        self.password = "mthvtrnksnqqlgjl"

    def send_email(self, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(from_addr=self.my_email, to_addrs="202303146701@alunos.ibmec.edu.br",
                                msg=message.encode('ascii', 'ignore'))
