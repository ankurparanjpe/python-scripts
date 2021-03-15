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
Subject: Bjoern Pricelist Error!

Bjoern Pricelist didnt found on the required path or not refreshed successfully. Please check manually!
"""

message_success = """From: <rncteam@brodos.net>
Subject: Bjoern Pricelist Success!

Bjoern Pricelist successfully uploaded on FTP! And a copy sent to required stakeholders.
"""



try:
    session = ftplib.FTP('212.68.72.35','72588','56fGh7Ds1')
    file = open(f'I:/Abteilungen/Reporting_und_Controlling/private/Preislisten/t_Björn/testingcsvxlsx/Preisliste Brodos {today}.csv','rb')                 
    session.storbinary(f'STOR Preisliste Brodos {today}.csv', file)    
    file.close()                                    
    session.quit()
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail('rncteam@brodos.net', 'ankur.paranjpe@brodos.net', message_success)

except Exception as e:
    print(e)
    smtpObj = smtplib.SMTP('172.17.7.101')
    smtpObj.sendmail('rncteam@brodos.net', 'rncteam@brodos.net', message_failed) 

