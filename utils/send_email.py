# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import smtplib
import json
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header
from logger import root_logger

logger = root_logger


try:
    with open("./config/mail.txt", 'r+') as mail_config_file:
        mail_config = json.load(mail_config_file)
        logger.info('mail_config_load')
        logger.info(mail_config)
except Exception, err:
    logger.error(err)
    raise


def send_mail(address=None, mail_body=None):
    logger.info('sending message')
    #формирование сообщения
    multi_msg = MIMEMultipart()
    multi_msg['From'] = Header(mail_config['message']['mail_from'], mail_config['message']['mail_coding'])
    multi_msg['To'] = Header(address, mail_config['message']['mail_coding'])
    multi_msg['Subject'] =  Header(mail_config['message']['mail_subj'], mail_config['message']['mail_coding'])
    msg = MIMEText(mail_body.encode(mail_config['message']['mail_coding']), 'html', mail_config['message']['mail_coding'])
    msg.set_charset(mail_config['message']['mail_coding'])
    multi_msg.attach(msg)
    logger.info('message create')
    logger.info(multi_msg)
    logger.info(msg)
    #отправка
    logger.info('sending msg')
    mailServer = smtplib.SMTP(mail_config['server']['smtp_server'], mail_config['server']['smtp_port'], timeout=30)
    if mail_config['server']['mail_use_tls']:
        mailServer.ehlo()
        mailServer.starttls()
    logger.info('mail.server.login')
    mailServer.login(mail_config['server']['smtp_address'], mail_config['server']['smtp_password'])
    logger.info('mail.server.send')
    mailServer.sendmail(mail_config['message']['mail_from'], mail_config['message']['mail_to'], multi_msg.as_string())
    mailServer.close()
    logger.info('message sended')
