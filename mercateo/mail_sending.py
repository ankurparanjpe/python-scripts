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
SUBJECT = "Preisliste Mercateo"
EMAIL_TO = ['Johanna.Neumann@brodos.de','geschaeftskunden@brodos.de','rncteam@brodos.net']
#EMAIL_TO = ['ankur.paranjpe@brodos.net','yash.joshi@brodos.net']


mercateo = os.path.getmtime('I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/t_belsimpel/xlsxcopies/belsimpel.xlsx')
mercateo = datetime.fromtimestamp(mercateo).strftime('%d-%m-%Y')


message_failed = """From: <rncteam@brodos.net>
Subject: Mercateo Pricelist Error!

Mercateo Pricelist didnt found on the required path or not refreshed successfully. Please check manually!
"""

try:
    if mercateo == today1:
        msg = MIMEMultipart()
        msg['Subject'] = SUBJECT 
        msg['From'] = 'rncteam@brodos.net'
        msg['To'] = ', '.join(EMAIL_TO)
        #msg['Bcc'] = ['distribution@brodos.de']
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open("I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/t_Mercateo/Mercateo_Preisliste.csv", "rb").read(),'UTF-8')
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="Mercateo_Preisliste.csv"')
        msg.attach(part)
        body = f"Hallo zusammen,\n\nanbei die heutige Preisliste, nach der Mercateo bestellen kann."
        part2 = MIMEText(body,'plain')
        msg.attach(part2)
        server = smtplib.SMTP('172.17.7.101')
        server.sendmail('rncteam@brodos.net', EMAIL_TO, msg.as_string())
        copyfile('I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/t_Mercateo/Mercateo_Preisliste.csv', 'I:/daten/bnet-imp/NORMAL_PRICEIMPORT/Mercateo_Preisliste.csv')
        
except Exception as e:
    print(e)
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail('rncteam@brodos.net', 'rncteam@brodos.net', message_failed) 


