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
SUBJECT = "Article Backlog"
EMAIL_TO = [
        'marc.goergens@brodos.de','Stefan.Vitzithum@brodos.de','Marcus.Brendl@brodos.de','frank.luettjohann@brodos.de','berlin@brodos.de','Oliver.Ascherl@brodos.de','Kevin.Lange@brodos.de','Marcel.Mundzeck@brodos.de',
        'Marcel.Thummet@brodos.de','Daniel.Fischer@brodos.de','stammdatenpflege@brodos.de','Lukas.Dorn@brodos.de','Vishal.Jagani@brodos.net','pmsupport@brodos.de','Rainer.Polster@brodos.de','yash.joshi@brodos.net','marc.goergens@brodos.de',
        'Vitalis.Becker@brodos.de','Bjoern.Roth@brodos.de','Nathalie.Hass@brodos.de','Tirth.Jani@brodos.net','Anna.Brusciano@brodos.de','Sales.Operations@brodos.de','Joy.Hemilton@brodos.net','zainul.khoja@brodos.net','Cathleen.Kretschmar@brodos.de',
        'Konzernkunden@brodos.de','Christina.Hierl@brodos.de','FH-Auftragsabwicklung@brodos.de','Christian.Hassa@brodos.de','produktmanagement_hardware@brodos.de','elektromaerkte@brodos.de','BO_EK&HW_TeamAnja@brodos.de','fachhandel@brodos.de','Susi.Herzog@brodos.de',
        'rncteam@brodos.net']
#EMAIL_TO = ['ankur.paranjpe@brodos.net','yash.joshi@brodos.net']
article_backlog = os.path.getmtime('I:/Abteilungen/Reporting_und_Controlling/private/Reportings/taeglich/Artikelrückstande/Artikelrückstände - Copy.xlsm')
article_backlog = datetime.fromtimestamp(article_backlog).strftime('%d-%m-%Y')


message_failed = """From: <rncteam@brodos.net>
Subject: Article backlog Error!

Article backlog file didnt found on the required path or not refreshed successfully. Please check manually!
"""

try:

    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT 
    msg['From'] = 'rncteam@brodos.net'
    msg['To'] = ', '.join(EMAIL_TO)

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("I:/Abteilungen/Reporting_und_Controlling/private/Reportings/taeglich/Artikelrückstande/xlsxcopies/Artikelrückstände.xlsx", "rb").read(),'UTF-8')
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="Artikelrueckstaende.xlsx"')
    msg.attach(part)
    body = f"Please find attached Article backlog file for {today1}."
    part2 = MIMEText(body,'plain')
    msg.attach(part2)
    server = smtplib.SMTP('172.17.7.101')

    server.sendmail('rncteam@brodos.net',EMAIL_TO, msg.as_string())
    print("done")
except Exception as e:
    print(e)
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail('rncteam@brodos.net', EMAIL_TO, message_failed) 


