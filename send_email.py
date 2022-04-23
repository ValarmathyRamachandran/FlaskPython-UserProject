from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import flash


def send_email(To, Subject, message, Token):
    # create message object instance
    msg = MIMEMultipart()

    message = message + Token

    # setup the parameters of the message
    password = "Test@12345"
    msg['From'] = "valarmathyb123@gmail.com"
    msg['To'] = To
    msg['Subject'] = Subject

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print("successfully sent email to %s:" % (msg['To']))
