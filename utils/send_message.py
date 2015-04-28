# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import smtplib
import json
from send_email import send_mail
import Skype4Py
from logger import root_logger


logger = root_logger
#переделать
#skype:
# name = "echo123"
#
# TIME_WAIT = 10  # пауза между посылками email, в секундах


 
#msg = MIMEText(mail_text.encode('cp1251'), 'plain', mail_coding)
def send_message(send_to, send_target, cars):
    logger.info('sending message')
    logger.info(send_to)
    cars_for_send = []
    for car in cars:
        if cars[car]["sended"] == False:
            cars_for_send.append('%s    %s    '%(cars[car]["name"], car))
            cars[car]["sended"] = True
            #print items[i]["sended"]
    try:
        if send_to == 'email':
            if cars_for_send:
                logger.info(cars_for_send)
                send_mail(send_target,  r'<br>'.join(cars_for_send))
            return cars
        elif send_to == 'skype':
            if cars_for_send:
                logger.info(cars_for_send)
                send_skype(send_target, '      '.join(cars_for_send))
            return cars
    except Exception, err:
        for car in cars:
            cars[car]["sended"] = False
        return cars
        logger.error(err)

    print "тип отправки %s временно не поддерживается"%send_to


def send_skype(address=None, mail_body=None):
    logger.info(address)
    logger.info(mail_body)
    skype = Skype4Py.Skype()
    if not skype.Client.IsRunning:
        logger.info('Starting Skype..')
        skype.Client.Start()
    logger.info('Connecting to Skype..')
    skype.Attach()
    Found =False
    for F in skype.Friends:
        #print  F.Handle, type(F.Handle), address, type(address), F.Handle == address
        if F.Handle == address:
            Found = True
            skype.CreateChatWith(F.Handle).SendMessage(mail_body)
            logger.info('message sended to %s'%F.Handle)
    if not Found:
        logger.error('cannot find %s'%address)
        raise Exception('cannot find %s'%address)

#Creating Skype object and assigning event handlers..
# skype = Skype4Py.Skype()
#
# # skype.OnAttachmentStatus = OnAttach
# # skype.OnCallStatus = OnCall
#
# # Starting Skype if it's not running already..
# if not skype.Client.IsRunning:
#     print 'Starting Skype..'
#     skype.Client.Start()
#
# # Attatching to Skype..
# print 'Connecting to Skype..'
# skype.Attach()
# #
# # Checking if what we got from command line parameter is present in our contact list
# Found = False
# for F in skype.Friends:
#     print F
#     print F.Handle
#     print dir(F)
#     print dir(skype.CreateChatWith(F.Handle).Messages.Item)
#     print skype.CreateChatWith(F.Handle).Messages
#     #skype.CreateChatWith(F.Handle).Messages()
#     for mess in skype.CreateChatWith(F.Handle).Messages:
#         print mess.FromHandle + ': ' + mess.Body
#     print skype.CreateChatWith(F.Handle).Messages[0].Body
#     x = str(skype.CreateChatWith(F.Handle).Messages[0].Body)
#
#     break
#
#     skype.CreateChatWith(F.Handle).Messages
# #     # skype.CreateChatWith(F.Handle).SendMessage('проверка работоспособности skype бота, если сообщение пришло, отведте какую-нибудь муру')
# #
# #     print dir(skype.CreateChatWith(F.Handle))
# #
# #     #skype.
# #
# # #
# # # # Create an instance of the Skype class.
# # # skype = Skype4Py.Skype()
# # #
# # # # Connect the Skype object to the Skype client.
# # # skype.Attach()
# # #
# # # # Obtain some information from the client and print it out.
# # # print 'Your full name:', skype.CurrentUser.FullName
# # # print 'Your contacts:'
# # # for user in skype.Friends:
# #     print '    ', user.FullName