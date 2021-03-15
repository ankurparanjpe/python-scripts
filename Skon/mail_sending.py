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
SUBJECT = "Preisliste brodos"
EMAIL_TO = ['christian.loewner@skon.de','Anna.Roraf@skon.de','rncteam@brodos.net']
#EMAIL_TO = ['ankur.paranjpe@brodos.net']
skon = os.path.getmtime('I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/t_skon/xlsxcopies/PRL skon.xlsx')
skon = datetime.fromtimestamp(skon).strftime('%d-%m-%Y')


message_failed = """From: <rncteam@brodos.net>
Subject: t_skon Pricelist Error!

t_skon Pricelist didnt found on the required path or not refreshed successfully. Please check manually!
"""

try:

    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT 
    msg['From'] = 'rncteam@brodos.net'
    msg['To'] = ', '.join(EMAIL_TO)
    #msg['Bcc'] = 'distribution@brodos.de'
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/t_skon/xlsxcopies/PRL skon.xlsx", "rb").read(),'UTF-8')
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="PRL skon.xlsx"')
    msg.attach(part)
    body = f"Guten Tag,\n anbei finden Sie unsere aktuelle Preisliste."
    part2 = MIMEText(body,'plain')
    msg.attach(part2)
    server = smtplib.SMTP('172.17.7.101')
    server.sendmail('rncteam@brodos.net', EMAIL_TO, msg.as_string())
    
except Exception as e:
    print(e)
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail('rncteam@brodos.net', 'rncteam@brodos.net', message_failed) 


