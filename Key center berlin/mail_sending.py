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


SUBJECT = "Ertragsauswertung"
EMAIL_TO = ['Stefanie.Leimberger@brodos.de']
#EMAIL_TO = ['ankur.paranjpe@brodos.net']

today1= datetime.today().strftime('%d-%m-%Y')
today = datetime.today().strftime('%Y.%m.%d')

message_failed = """From: <yash.joshi@brodos.de>
Subject: Key Account Berlin Pricelist Error!

Key Account Berlin Pricelist didnt found on the required path or not refreshed successfully. Please check manually!
"""

try:

    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT 
    msg['From'] = 'yash.joshi@brodos.net'
    msg['To'] = ', '.join(EMAIL_TO)
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(f"I:/Abteilungen/Backoffice/Auftragsverwaltung-Kundensupport/public/KAM Online_&_LEH/Ertragsauswertung/Archiv/{today}.xlsx", "rb").read(),'UTF-8')
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={today}.xlsx')
    msg.attach(part)
    body = f'Good Morning,\nYou can find the new "Ertragsauswertung" here:\nI:\Abteilungen\Backoffice\Auftragsverwaltung-Kundensupport\public\KAM Online_&_LEH\Ertragsauswertung'
    part2 = MIMEText(body,'plain')
    msg.attach(part2)
    server = smtplib.SMTP('172.17.7.101')
    server.sendmail('yash.joshi@brodos.net', EMAIL_TO, msg.as_string())
    print("done")

except Exception as e:
    print(e)
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail('yash.joshi@brodos.de', 'ankur.paranjpe@brodos.net', message_failed) 


