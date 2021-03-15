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
import email.message

today1= datetime.today().strftime('%d-%m-%Y')
today = datetime.today().strftime('%d.%m.%Y')
SUBJECT = "Preisliste Brodos"
EMAIL_TO = 'rncteam@brodos.net',
EMAIL_TO1 ='thomas.entian@hificomponents.com',
EMAIL_TO2 ='info@urcover.com',
EMAIL_TO3 ='einkauf@agi-akku.de',
EMAIL_TO4 ='do@inteldo.de',
EMAIL_TO5 ='info@watec-mobile.com',
EMAIL_TO6 ='MB@handyparadies.de',
EMAIL_TO7 ='bora@talksky.de',
EMAIL_TO8 ='kundenbestellungen-baiersdorf@brodos.de',
EMAIL_TO9 ='nikolaos.botsios@michael-telecom.de',
EMAIL_TO10 ='andrea.goettner@hificomponents.com',
EMAIL_TO11 ='kuechel@mpsmobile.de',
EMAIL_TO12 ='Florian.Riedle@brodos.de',
EMAIL_TO13 ='Martin.Herm@brodos.de'
EMAIL_TO14 ='m.mester@handytreff.de'

#EMAIL_TO = ['rncteam@brodos.net']
#EMAIL_TO1 = ['sahebaz.kazi@brodos.net']
#EMAIL_TO2 = ['ankur.paranjpe@brodos.net']
#EMAIL_TO3 = ['rncteam@brodos.net']

message_failed = """From: <rncteam@brodos.net>
Subject: Björn Pricelist Error!

Björn Pricelist didnt found on the required path or not refreshed successfully. Please check manually!
"""

try:

    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT 
    msg['From'] = 'rncteam@brodos.net'
    msg['To'] = ', '.join(EMAIL_TO)
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(f"I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/t_Björn/testingcsvxlsx/Preisliste Brodos 27.01.2021.csv", "rb").read(),'UTF-8')
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="Preisliste Brodos {today}.csv"')
    msg.attach(part)
    
    part1 = MIMEBase('application', "octet-stream")
    part1.set_payload(open(f"I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/t_Björn/testingcsvxlsx/Preisliste Brodos 27.01.2021.xlsx", "rb").read(),'UTF-8')
    encoders.encode_base64(part1)
    part1.add_header('Content-Disposition', f'attachment; filename="Preisliste Brodos {today}.xlsx"')
    msg.attach(part1)

    
    body = f"""Guten Tag,

anbei erhalten sie die aktuelle Preisliste.
Bei Fragen wenden Sie sich gerne an Vertrieb-Hardware@brodos.
de-Änderungen und Irrtümer vorbehalten"""
    part2 = MIMEText(body,'plain')
    msg.attach(part2)
    server = smtplib.SMTP('172.17.7.101')
    server.sendmail('rncteam@brodos.net', EMAIL_TO , msg.as_string())
    server.sendmail('rncteam@brodos.net', EMAIL_TO1, msg.as_string())
    server.sendmail('rncteam@brodos.net', EMAIL_TO2, msg.as_string())
    server.sendmail('rncteam@brodos.net', EMAIL_TO3, msg.as_string())
    server.sendmail('rncteam@brodos.net', EMAIL_TO4, msg.as_string())
    server.sendmail('rncteam@brodos.net', EMAIL_TO5, msg.as_string())
    server.sendmail('rncteam@brodos.net', EMAIL_TO6, msg.as_string())
    server.sendmail('rncteam@brodos.net', EMAIL_TO7, msg.as_string())
    server.sendmail('rncteam@brodos.net', EMAIL_TO8, msg.as_string())
    server.sendmail('rncteam@brodos.net', EMAIL_TO9, msg.as_string())
    server.sendmail('rncteam@brodos.net', EMAIL_TO10, msg.as_string())
    server.sendmail('rncteam@brodos.net', EMAIL_TO11, msg.as_string())
    server.sendmail('rncteam@brodos.net', EMAIL_TO12, msg.as_string())
    server.sendmail('rncteam@brodos.net', EMAIL_TO13, msg.as_string())
    server.sendmail('rncteam@brodos.net', EMAIL_TO14, msg.as_string())
        
except Exception as e:
    print(e)
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail('rncteam@brodos.net', 'rncteam@brodos.net', message_failed) 




