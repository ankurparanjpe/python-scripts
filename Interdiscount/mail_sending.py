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
SUBJECT = "Pricelist brodos"
EMAIL_TO = ['nicole.scheffel@interdiscount.ch']
#EMAIL_TO = ['yash.joshi@brodos.net']

interdiscount = os.path.getmtime('I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/t_interdiscount/xlsxcopy/PRL interdiscount.xlsx')
interdiscount = datetime.fromtimestamp(interdiscount).strftime('%d-%m-%Y')


message_failed = """From: <rncteam@brodos.net>
Subject: interdiscount Pricelist Error!

interdiscount Pricelist didnt found on the required path or not refreshed successfully. Please check manually!
"""

try:
    if interdiscount == today1:
        msg = MIMEMultipart()
        msg['Subject'] = SUBJECT 
        msg['From'] = 'rncteam@brodos.net'
        msg['To'] = ', '.join(EMAIL_TO)
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open("I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/t_interdiscount/xlsxcopy/PRL interdiscount.xlsx", "rb").read(),'UTF-8')
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="PRL interdiscount.xlsx"')
        msg.attach(part)
        body = f"Guten Tag,\nanbei finden Sie unsere aktuelle Preisliste."
        part2 = MIMEText(body,'plain')
        msg.attach(part2)
        server = smtplib.SMTP('172.17.7.101')
        server.sendmail('rncteam@brodos.net', EMAIL_TO, msg.as_string())
    
except Exception as e:
    print(e)
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail('rncteam@brodos.net', 'rncteam@brodos.net', message_failed) 


