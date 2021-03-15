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
today = datetime.today().strftime('%Y%m%d')
SUBJECT = "stockfile_1000"
EMAIL_TO = ['conrad@brodos.de', 'Kevin.Lange@brodos.de','Marcel.Mundzeck@brodos.de','rncteam@brodos.net']
#EMAIL_TO = ['ankur.paranjpe@brodos.net','yash.joshi@brodos.net']


message_failed = """From: <rncteam@brodos.net>
Subject: Conrad Pricelist Error!

Conrad Pricelist didnt found on the required path or not refreshed successfully. Please check manually!
"""

try:

    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT 
    msg['From'] = 'rncteam@brodos.net'
    msg['To'] = ', '.join(EMAIL_TO)
    #msg['Bcc'] = ['distribution@brodos.de']
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(f"I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/t_Conrad/testingcsvs/96020330_1000_{today}.csv", "rb").read(),'UTF-8')
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="96020330_1000_{today}.csv"')
    msg.attach(part)
    body = f"""Sehr geehrte Damen und Herren,\n\nanbei erhalten Sie unsere aktuelle Preisliste als csv.
\nBei Fragen wenden Sie sich gerne an meine Kollegen Kevin Lange (kevin.lange@brodos.de) und Marcel Mundzeck (marcel.mundzeck@brodos.de)"""
    part2 = MIMEText(body,'plain')
    msg.attach(part2)
    server = smtplib.SMTP('172.17.7.101')
    server.sendmail('rncteam@brodos.net', EMAIL_TO, msg.as_string())
        
except Exception as e:
    print(e)
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail('rncteam@brodos.net', 'rncteam@brodos.net', message_failed) 


