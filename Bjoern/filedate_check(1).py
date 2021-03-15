import ftplib
from  datetime import date,datetime,timedelta
import requests
from zipfile import ZipFile
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from subprocess import call
from win32com.client import Dispatch

yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y%m%d')
today1 = datetime.today().strftime('%d-%m-%Y')
email_user = 'rncteam@brodos.net'
email_send = ['ankur.paranjpe@brodos.net']
message_file = """From: <rncteam@brodos.net>
Subject: Björn Pricelist Data/source Error!

One of the files for Björn Pricelist file source are older or not available in required path!
"""

try:
    
    artzub = os.path.getmtime(f'I:/Abteilungen/Reporting_und_Controlling/private/Datenbanken/J DBF/ARTZUB.txt')
    artikel = os.path.getmtime(f'I:/Abteilungen/Reporting_und_Controlling/private/Datenbanken/J DBF/ARTIKEL.txt')
    lagreich = os.path.getmtime(f'I:/Abteilungen/Reporting_und_Controlling/private/Datenbanken/J DBF/LAGREICH.txt')
    produkte = os.path.getmtime(f'I:/Abteilungen/Reporting_und_Controlling/private/Datenbanken/Eigene/PRODUKTE.xlsx')
    Kundenrueckstaende = os.path.getmtime(f'I:/Abteilungen/Reporting_und_Controlling/private/Datenbanken/Rueckstaende/Kundenrueckstaende.csv')
    
    
    
    artzub = datetime.fromtimestamp(artzub).strftime('%d-%m-%Y')
    artikel = datetime.fromtimestamp(artikel).strftime('%d-%m-%Y')
    lagreich = datetime.fromtimestamp(lagreich).strftime('%d-%m-%Y')
    produkte = datetime.fromtimestamp(produkte).strftime('%d-%m-%Y')
    Kundenrueckstaende = datetime.fromtimestamp(Kundenrueckstaende).strftime('%d-%m-%Y')
    
    if artzub and artikel and produkte and Kundenrueckstaende == today1:
        xl = Dispatch("Excel.Application")
        xl.Visible = True
        wb = xl.Workbooks.Open(r'I:\\Abteilungen\\Reporting_und_Controlling\\private\\Preislisten\\t_Björn\\PRL Reporting PQ - Copy.xlsm')

        print('yes available')
    else:
        print('nope')
        smtpObj = smtplib.SMTP('172.17.7.101')
        smtpObj.sendmail(email_user, email_send, message_file) 

except Exception as e:
    print('file error')
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail(email_user, email_send, message_file) 


