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

today1= datetime.today().strftime('%d-%m-%Y')
today = datetime.today().strftime('%m%d')
SUBJECT = "Preisliste HDK Success"

EMAIL_TO = ['ankur.paranjpe@brodos.net','rncteam@brodos.net']


message_failed = """From: <rncteam@brodos.net>
Subject: HDK Pricelist Error!

HDK Pricelist didnt found on the required path or not refreshed successfully. Please check manually!
"""

try:
    copyfile(f'I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/t_HDK/testingcsvs/HDK_{today}_1.csv', f'I:/daten/bnet-imp/NORMAL_PRICEIMPORT/BC_{today}_1.csv')
    copyfile(f'I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/t_HDK/testingcsvs/HDK_{today}_2.csv', f'I:/daten/bnet-imp/NORMAL_PRICEIMPORT/BC_{today}_2.csv')
    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT 
    msg['From'] = 'rncteam@brodos.net'
    msg['To'] = ', '.join(EMAIL_TO)
    #msg['Bcc'] = ['distribution@brodos.de']
    #part = MIMEBase('application', "octet-stream")
    #part.set_payload(open("I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/t_Mercateo/Mercateo_Preisliste.csv", "rb").read(),'UTF-8')
    #encoders.encode_base64(part)
    #part.add_header('Content-Disposition', 'attachment; filename="Mercateo_Preisliste.csv"')
    #msg.attach(part)
    body = f"Hallo,\n\nHDK files are copied to 'NORMAL_PRICEIMPORT' folder."
    part2 = MIMEText(body,'plain')
    msg.attach(part2)
    server = smtplib.SMTP('172.17.7.101')
    server.sendmail('rncteam@brodos.net', EMAIL_TO, msg.as_string())
except Exception as e:
    print(e)
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail('rncteam@brodos.net', 'rncteam@brodos.net', message_failed) 


