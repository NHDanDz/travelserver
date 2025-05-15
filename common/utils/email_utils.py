#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email(subject, content, receivers):
    """
    Send email function
    """
    try:
        # Third-party SMTP service
        mail_host = "smtp.example.com"  # Set the server
        mail_user = "username"  # Username
        mail_pass = "password"  # Password

        sender = 'from@example.com'
        
        message = MIMEText(content, 'plain', 'utf-8')
        message['From'] = Header("TravelGPT", 'utf-8')
        message['To'] = Header("User", 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')

        # For testing purposes, return True without actually sending
        return True
        
        # Uncomment below to actually send emails
        """
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 is the SMTP port number
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        return True
        """
    except smtplib.SMTPException:
        print("Error: Unable to send email")
        return False