import ftplib
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from  datetime import date,datetime,timedelta

today = datetime.today().strftime('%d.%m.%Y')


message_failed = """From: <rncteam@brodos.net>
Subject: Bechtle Pricelist Error!

Bechtle Pricelist didnt found on the required path or not refreshed successfully. Please check manually!
"""

message_success = """From: <rncteam@brodos.net>
Subject: Bechtle Pricelist Success!

Bechtle Pricelist successfully uploaded on FTP! And a copy sent to required stakeholders.
"""



try:
    session = ftplib.FTP('ftp.brodos.net','bechtle','iWi4ahng6kuqu2oi1Ofa')
    file = open(f'I:/Abteilungen/Konzern-und-Geschaeftskunden/public/A Preislisten CC + Bechtle + Mercateo/xlsxcopies/Bechtle-brodos.csv','rb')
    session.storbinary(f'STOR Bechtle-brodos.csv', file)    
    file.close()                                    
    session.quit()
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail('rncteam@brodos.net', 'rncteam@brodos.net', message_success)

except Exception as e:
    print(e)
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail('rncteam@brodos.net', 'rncteam@brodos.net', message_failed) 

