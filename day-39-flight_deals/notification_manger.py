import smtplib
import os


class NotificationManager():

    def __init__(self):
        self.my_email = "daisiduuke@gmail.com"
        self.app_password = os.getenv("DAISI_PASSWORD")

    def send_mail(self, subject: str, body: str, to_email: str):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.app_password)
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs=to_email,
                msg=f"Subject:{subject}\n\n{body}")



