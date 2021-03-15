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

today1= datetime.today().strftime('%Y.%m.%d')
today = datetime.today().strftime('%d-%m-%Y')
SUBJECT = f"Brodos Pricelist citytalk {today}"
EMAIL_TO = ['hardware@citytalk.gmbh','Vertrieb-Hardware@brodos.de','rncteam@brodos.net']
#EMAIL_TO = ['ankur.paranjpe@brodos.net','yash.joshi@brodos.net']


message_failed = """From: <rncteam@brodos.net>
Subject: City Talk Pricelist Error!

City Talk Pricelist didnt found on the required path or not refreshed successfully. Please check manually!
"""

try:
    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT 
    msg['From'] = 'rncteam@brodos.net'
    msg['To'] = ', '.join(EMAIL_TO)
    #msg['Bcc'] = ['distribution@brodos.de']
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(f"I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/2xm_City Talk/testingxlsx/Brodos PRL {today1}.xlsx", "rb").read(),'UTF-8')
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="Brodos PRL {today1}.xlsx"')
    msg.attach(part)
    body = f"""Hallo Herr Zintl,\n\n
anbei sende ich Ihnen wie gewünscht eine Liste mit aktuellen Preisen und Lagerbeständen aus dem Brodos Lager.\n\n
Sie sind dazu verpflichtet die Liste vertraulich zu behandeln und nicht an Dritte weiter zu geben.\n\n
Alle Bestellungen von Ihnen sind verbindlich und werden sofort bearbeitet und versendet.\n\n
Für alle weiteren Richtlinien zu Zahlungsbedingungen und Lieferbedingungen gelten unsere AGBs."""
    part2 = MIMEText(body,'plain')
    msg.attach(part2)
    server = smtplib.SMTP('172.17.7.101')
    server.sendmail('rncteam@brodos.net', EMAIL_TO, msg.as_string())
    
except Exception as e:
    print(e)
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail('rncteam@brodos.net', 'rncteam@brodos.net', message_failed) 


