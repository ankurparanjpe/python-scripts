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
from shutil import copyfile
from glob import glob

today1= datetime.today().strftime('%d-%m-%Y')
today = datetime.today().strftime('%d.%m.%Y')
SUBJECT = "Preisliste Brodos AG"
EMAIL_TO = ['Nicole.Letzel@computacenter.com']
#EMAIL_TO = ['ankur.paranjpe@brodos.net','rncteam@brodos.net']


message_failed = """From: <rncteam@brodos.net>
Subject: Computer center Pricelist Error!

Computer center Pricelist didnt found on the required path or not refreshed successfully. Please check manually!
"""

try:

    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT 
    msg['From'] = 'rncteam@brodos.net'
    msg['To'] = ', '.join(EMAIL_TO)
    #msg['Bcc'] = ['distribution@brodos.de']
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(f"I:/Abteilungen/Konzern-und-Geschaeftskunden/public/A Preislisten CC + Bechtle + Mercateo/ComputacenterPRL.csv", "rb").read(),'UTF-8')
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="ComputacenterPRL.csv"')
    msg.attach(part)   
    body = f"""Sehr geehrte Frau Letzel,

anbei unsere heutige Preisliste.

Mit besten Grüßen,
Brodos Reporting Team"""
    part2 = MIMEText(body,'plain')
    msg.attach(part2)
    server = smtplib.SMTP('172.17.7.101')
    server.sendmail('rncteam@brodos.net', EMAIL_TO, msg.as_string())
    
        
except Exception as e:
    print(e)
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail('rncteam@brodos.net', 'rncteam@brodos.net', message_failed) 


