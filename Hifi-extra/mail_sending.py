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
today = datetime.today().strftime('%d.%m.%Y')
SUBJECT = "Brodos Preisliste"
EMAIL_TO = ['Johanna.Neumann@brodos.de', 'sascha.koelpien@brodos.de','frank.stegt@hifi-extra.de','yash.joshi@brodos.net']
#EMAIL_TO = ['ankur.paranjpe@brodos.net','yash.joshi@brodos.net']


#highfi = os.path.getmtime(f'I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/t_hifi-extra/testingxlsx/Brodos_PRL {today}.xlsx')
#highfi = datetime.fromtimestamp(highfi).strftime('%d-%m-%Y')


message_failed = """From: <rncteam@brodos.net>
Subject: HighFi-Extra Pricelist Error!

HighFi-Extra Pricelist didnt found on the required path or not refreshed successfully. Please check manually!
"""

try:

    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT 
    msg['From'] = 'rncteam@brodos.net'
    msg['To'] = ', '.join(EMAIL_TO)
    #msg['Bcc'] = ['distribution@brodos.de']
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(f"I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/t_hifi-extra/testingxlsx/Brodos_PRL {today}.xlsx", "rb").read(),'UTF-8')
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="Brodos_PRL {today}.xlsx"')
    msg.attach(part)
    body = f"Guten Tag,\n\nanbei erhalten Sie die aktuelle Preisliste.\n\n-Änderungen und Irrtümer vorbehalten"
    part2 = MIMEText(body,'plain')
    msg.attach(part2)
    server = smtplib.SMTP('172.17.7.101')
    server.sendmail('rncteam@brodos.net', EMAIL_TO, msg.as_string())
        
except Exception as e:
    print(e)
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail('rncteam@brodos.net', 'rncteam@brodos.net', message_failed) 


