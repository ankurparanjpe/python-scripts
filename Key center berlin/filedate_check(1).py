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
Subject: Key Account Berlin File Data/source Error!

One of the files for Key Account Berlin file source are older or not available in required path!
"""

try:
    
    konditionsuebersicht = os.path.isfile(f'I:/Abteilungen/Backoffice/Auftragsverwaltung-Kundensupport/public/KAM Online_&_LEH/Ertragsauswertung/Data/Konditionsübersicht REPORTINg.xlsm')
    keyaccount = os.path.isfile(f'I:/Abteilungen/Backoffice/Auftragsverwaltung-Kundensupport/public/KAM Online_&_LEH/Ertragsauswertung/Data/Konditionsübersicht REPORTINg.xlsm')
    auftrag = os.path.getmtime(f'I:/Abteilungen/Reporting_und_Controlling/private/Reportings/taeglich/Ertragsauswertung Key Account Berlin/Data/AUFTRAG.txt')
    

    auftrag = datetime.fromtimestamp(auftrag).strftime('%d-%m-%Y')


    if auftrag == today1:
        xl = Dispatch("Excel.Application")
        xl.Visible = True
        wb = xl.Workbooks.Open(r'I:\\Abteilungen\\Reporting_und_Controlling\\private\\Reportings\\taeglich\\Ertragsauswertung Key Account Berlin\\Data\\Ertragsauswertung Key Account Berlin - Copy.xlsm')
        print('yes available')
    else:
        print('nope')
        smtpObj = smtplib.SMTP('172.17.7.101')
        smtpObj.sendmail(email_user, email_send, message_file) 

    
    

except Exception as e:
    print('file error')
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail(email_user, email_send, message_file) 


