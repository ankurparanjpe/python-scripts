import ftplib
from  datetime import date,datetime
import requests
from zipfile import ZipFile
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

today1= datetime.today().strftime('%d-%m-%Y')

email_user = 'rncteam@brodos.net'
email_send = ['rncteam@brodos.net']
message_file = """From: <rncteam@brodos.net>
Subject: Stocklist_vba Error!

Stocklist_vba or stocklist file didnt refreshed as expected. Please check manually!
"""

message_sucess = """From: <rncteam@brodos.net>
Subject: Stocklist File Sucess!

Stocklist Report is successfully generated/Refreshed. ENJOY!!!
"""

"""Checking weather the files are updated"""
try:
    stocklist_vba = os.path.getmtime('I:/Abteilungen/Reporting_und_Controlling/private/Datenbanken/Eigene/STOCKLIST VBA.xlsm')
    stocklist = os.path.getmtime('I:/Abteilungen/Reporting_und_Controlling/private/Datenbanken/Eigene/STOCKLIST.xlsx')
    stocklist_vba = datetime.fromtimestamp(stocklist_vba).strftime('%d-%m-%Y')
    stocklist = datetime.fromtimestamp(stocklist).strftime('%d-%m-%Y')

    if stocklist_vba and stocklist == today1:
        smtpObj = smtplib.SMTP('172.17.7.101')
        smtpObj.sendmail(email_user, email_send, message_sucess)
        print('Stocklist Report is successfully prepared')
    else:
        print('failed')
        smtpObj = smtplib.SMTP('172.17.7.101')
        smtpObj.sendmail(email_user, email_send, message_file) 
except Exception as e:
    print('failed')
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail(email_user, email_send, message_file) 


