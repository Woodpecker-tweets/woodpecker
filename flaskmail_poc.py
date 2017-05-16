#!/usr/bin/python3
from flask import Flask
#from flaskext.mail import Mail, Message
from flask_mail import Mail, Message
from os import getenv

app =Flask(__name__)
mail=Mail(app)

usr = 'woodpecker.tweets@gmail.com',
app.config.update(
    DEBUG=True,
    #EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = "woodpecker.tweets",
    MAIL_PASSWORD = "b8sm2YNOzB" # change to access via getenv('MAILPWD')
    )

mail=Mail(app)

@app.route("/")
def index():
    msg = Message('Hello',
                  sender=("Woodpecker", "woodpecker.tweets@gmail.com"),
                  recipients = ['95@holbertonschool.com'])
    msg.subject = "Hello Test"
    msg.body = "This is the email body"
    mail.send(msg)
    return ("Sent")

if __name__ == "__main__":
    app.run()
