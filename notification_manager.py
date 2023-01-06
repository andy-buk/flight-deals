import smtplib
from email.mime.text import MIMEText

my_email = "email@gmail.com"
password = "your password"


class NotificationManager:
    def send_sms(self, message):
        new_message = MIMEText(message)
        new_message["Subject"] = "Low price alert!"
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="recipient",
                                msg=new_message.as_string())
