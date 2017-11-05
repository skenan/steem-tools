#!/usr/bin/python
# -*- coding: utf-8 -*-

import sendgrid
from sendgrid.helpers.mail import *
from config import Key
from log import Log
logger = Log()

apikey = Key['send_grid']['key']
sg = sendgrid.SendGridAPIClient(apikey=apikey)


def send_email(email_from_file, code):
    from_email = Email(Key['send_grid']['from_email'])
    to_email = Email(email_from_file)
    subject = "你的CNsteem账号审核通过"
    message = "账号注册地址：https://cnsteem.com/start/%s" % code
    content = Content("text/plain", message)
    mail = Mail(from_email, subject, to_email, content)
    try:
        response = sg.client.mail.send.post(request_body=mail.get())
    except:
        logger.warning("To_Email: %s failed" % email_from_file)
        return
    logger.info("To_Email: %s, status code: %s" % (email_from_file, response.status_code))


with open('email.txt', 'r') as file:
    for line in file:
        (email_from_file, code) = line.split()
        send_email(email_from_file, code)
