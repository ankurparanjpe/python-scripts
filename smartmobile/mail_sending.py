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
#EMAIL_TO = ['ankur.paranjpe@brodos.net','yash.joshi@brodos.net']
EMAIL_TO = ['preisimport@smart-mobile.at','preisimport@smart-mobile.at','rncteam@brodos.net']

message_failed = """From: <rncteam@brodos.net>
Subject: Smartmobile AT Pricelist Error!

Smartmobile AT Pricelist didnt found on the required path or not refreshed successfully. Please check manually!
"""

try:
    smartmobile = os.path.getmtime('I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/t_Smartmobile AT/xlsxcopies/Smartmobile.xlsx')
    smartmobile = datetime.fromtimestamp(smartmobile).strftime('%d-%m-%Y')
    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT 
    msg['From'] = 'rncteam@brodos.net'
    msg['To'] = ', '.join(EMAIL_TO)
    #msg['Bcc'] = 'distribution@brodos.de'
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/t_Smartmobile AT/xlsxcopies/Smartmobile.xlsx", "rb").read(),'UTF-8')
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="Smartmobile.xlsx"')
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


